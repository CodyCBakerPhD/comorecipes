// Assembles the deployable site into dist/ (TypeScript port of the Python
// `generate_html_recipes` CLI — byte-for-byte identical output):
//   1. renders docs/recipes/*.yaml into dist/formatted_recipes/*.html,
//   2. generates the alphabetized dist/index.html,
//   3. generates the dist/manifests/ database manifests and their hashes,
//   4. copies the raw recipe/ingredient databases and CNAME,
//   5. adds .nojekyll so GitHub Pages serves the files verbatim (no Jekyll).
//
// Run with `npm run build` (requires Node >= 22.18 for native type stripping).

import { createHash } from "node:crypto";
import { cpSync, mkdirSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

import { parse } from "yaml";

interface RawMeasurement {
  amount: string | number;
  unit?: string;
  prefix?: string;
  suffix?: string;
  ingredient: string;
}

interface RawRecipe {
  name: string;
  tags?: string[];
  measurements: RawMeasurement[];
  instructions: string[];
  notes?: string[];
}

interface RawIngredient {
  name: string;
  portions_text?: string;
}

const repoRoot = dirname(dirname(fileURLToPath(import.meta.url)));
const docsDir = join(repoRoot, "docs");
const distDir = join(repoRoot, "dist");

function yamlStems(directory: string): string[] {
  return readdirSync(directory)
    .filter((fileName) => fileName.endsWith(".yaml"))
    .map((fileName) => fileName.slice(0, -".yaml".length))
    .sort();
}

function loadYaml<ParsedShape>(filePath: string): ParsedShape {
  return parse(readFileSync(filePath, "utf-8")) as ParsedShape;
}

// The special portions text of registered ingredients, e.g. "cloves" for "garlic".
const portionsTextByIngredientName = new Map<string, string>();
const ingredientsDir = join(docsDir, "ingredients");
for (const stem of yamlStems(ingredientsDir)) {
  const ingredient = loadYaml<RawIngredient>(join(ingredientsDir, `${stem}.yaml`));
  if (ingredient.portions_text != null) {
    portionsTextByIngredientName.set(ingredient.name, ingredient.portions_text);
  }
}

function getRenderedUnits(measurement: RawMeasurement): string {
  if (measurement.amount === "enough") {
    return "";
  }
  const portionsText = portionsTextByIngredientName.get(measurement.ingredient);
  if (measurement.unit === "portions" && portionsText != null) {
    return portionsText;
  }
  return measurement.unit ?? "";
}

// Markdown-like recipe page structure, mirroring `Recipe.to_html_file`.
function renderRecipeHtml(recipe: RawRecipe): string {
  const disallowedUnits = new Set(["", "portions"]);

  let html = '<p><a href="../index.html">Back to Recipe Index</a></p>\n\n';
  html += `<h1>${recipe.name}</h1>\n\n`;

  if (recipe.tags != null) {
    html += `<p>Tags: ${recipe.tags.join(", ")}</p>\n\n\n\n`;
  }

  html += "<br>\n";
  html += "<h2>Ingredients</h2>\n\n";
  for (const measurement of recipe.measurements) {
    html += `<p>${measurement.amount}`;

    const renderedUnits = getRenderedUnits(measurement);
    if (!disallowedUnits.has(renderedUnits)) {
      html += ` ${renderedUnits}`;
    }

    if (measurement.prefix != null) {
      html += ` ${measurement.prefix}`;
    }

    html += ` ${measurement.ingredient}`;

    if (measurement.suffix != null) {
      html += ` ${measurement.suffix}`;
    }

    html += "</p>\n";
  }

  if (recipe.notes != null) {
    html += "\n\n\n<br>\n";
    html += "<h2>Notes</h2>\n\n";
    for (const note of recipe.notes) {
      html += `<p>${note}</p>\n`;
    }
  }

  html += "\n\n\n<h2>Instructions</h2>\n\n";
  for (const instruction of recipe.instructions) {
    html += `<p>${instruction}</p>\n`;
  }

  return html;
}

rmSync(distDir, { recursive: true, force: true });
mkdirSync(join(distDir, "formatted_recipes"), { recursive: true });
mkdirSync(join(distDir, "manifests"), { recursive: true });

// All formatted HTML recipes for GitHub Pages
const alphabetizedRelativePathToRecipeName = new Map<string, Map<string, string>>();
const recipesDir = join(docsDir, "recipes");
for (const fileStem of yamlStems(recipesDir)) {
  const recipe = loadYaml<RawRecipe>(join(recipesDir, `${fileStem}.yaml`));
  const startingLetter = recipe.name[0].toUpperCase();

  const relativeHtmlPath = `formatted_recipes/${fileStem}.html`;
  let relativePathToRecipeName = alphabetizedRelativePathToRecipeName.get(startingLetter);
  if (relativePathToRecipeName == null) {
    relativePathToRecipeName = new Map<string, string>();
    alphabetizedRelativePathToRecipeName.set(startingLetter, relativePathToRecipeName);
  }
  relativePathToRecipeName.set(relativeHtmlPath, recipe.name);

  writeFileSync(join(distDir, relativeHtmlPath), renderRecipeHtml(recipe));
}

// Index file for GitHub Pages
let index = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recipe Index</title>
    <style>
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 5px;
        }
        .section {
            break-inside: avoid;
        }
    </style>
</head>
<body>
    <h1>Recipe Index</h1>
    <div class="grid-container">
`;
for (const [startingLetter, relativePathToRecipeName] of alphabetizedRelativePathToRecipeName) {
  index += '        <div class="section">\n';
  index += `            <h2>${startingLetter}</h2>\n`;
  index += "            <ul>\n";
  for (const [relativePath, recipeName] of relativePathToRecipeName) {
    index += `            <li><a href="${relativePath}">${recipeName}</a></li>\n`;
  }
  index += "            </ul>\n";
  index += "        </div>\n\n";
}
index += "    </div>\n</body>\n</html>\n";
writeFileSync(join(distDir, "index.html"), index);

// Hidden manifest files
const databases = ["recipes", "ingredients"];
for (const database of databases) {
  const databaseDir = join(docsDir, database);
  let manifest = "";
  for (const fileStem of yamlStems(databaseDir)) {
    const digest = createHash("md5").update(readFileSync(join(databaseDir, `${fileStem}.yaml`))).digest("hex");
    manifest += `${fileStem}: ${digest}\n`;
  }

  const manifestFilePath = join(distDir, "manifests", `${database}.yaml`);
  writeFileSync(manifestFilePath, manifest);

  const manifestHash = createHash("md5").update(readFileSync(manifestFilePath)).digest("hex");
  writeFileSync(join(distDir, "manifests", `${database}_hash.txt`), `${manifestHash}\n`);
}

// Raw databases are downloaded by the desktop app, so they ship with the site
for (const database of databases) {
  cpSync(join(docsDir, database), join(distDir, database), { recursive: true });
}

cpSync(join(docsDir, "CNAME"), join(distDir, "CNAME"));

// An empty .nojekyll file tells GitHub Pages to skip Jekyll entirely.
writeFileSync(join(distDir, ".nojekyll"), "");

console.log("Site built into dist/");
