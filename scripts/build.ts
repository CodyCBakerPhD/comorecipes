// Assembles the deployable site into dist/ (TypeScript port of the Python
// `generate_html_recipes` CLI — byte-for-byte identical output):
//   1. renders docs/recipes/*.yaml into styled dist/formatted_recipes/*.html,
//   2. generates the alphabetized dist/index.html with its live search filter,
//   3. copies the shared stylesheet and favicon from docs/assets into dist/assets,
//   4. generates the dist/manifests/ database manifests and their hashes,
//   5. copies the raw recipe/ingredient databases,
//   6. adds .nojekyll so GitHub Pages serves the files verbatim (no Jekyll).
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

// Mirrors Python's `html.escape` (quote=True) so output stays byte-identical.
function escapeHtml(text: string): string {
  return text
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#x27;");
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

// Styled recipe page structure, mirroring `Recipe.to_html_file`.
function renderRecipeHtml(recipe: RawRecipe): string {
  const escapedName = escapeHtml(recipe.name);
  const htmlLines = [
    "<!DOCTYPE html>",
    '<html lang="en">',
    "<head>",
    '    <meta charset="UTF-8">',
    '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
    `    <title>${escapedName} · CoMo Recipes</title>`,
    '    <link rel="icon" href="../assets/como_icon.ico">',
    '    <link rel="stylesheet" href="../assets/style.css">',
    "</head>",
    '<body class="recipe-page">',
    '    <nav class="top-bar">',
    '        <a class="brand" href="../index.html">CoMo Recipes</a>',
    '        <a class="back-link" href="../index.html">&larr; Recipe Index</a>',
    "    </nav>",
    '    <main class="recipe">',
    '        <header class="recipe-header">',
    `            <h1>${escapedName}</h1>`,
  ];

  if (recipe.tags != null) {
    htmlLines.push('            <ul class="tag-list">');
    for (const tag of recipe.tags) {
      htmlLines.push(`                <li class="tag">${escapeHtml(tag)}</li>`);
    }
    htmlLines.push("            </ul>");
  }

  htmlLines.push(
    "        </header>",
    '        <div class="recipe-body">',
    '            <section class="ingredients">',
    "                <h2>Ingredients</h2>",
    '                <ul class="ingredient-list">',
  );

  const disallowedUnits = new Set(["", "portions"]);
  for (const measurement of recipe.measurements) {
    let amountText = `${measurement.amount}`;

    const renderedUnits = getRenderedUnits(measurement);
    if (!disallowedUnits.has(renderedUnits)) {
      amountText += ` ${renderedUnits}`;
    }

    const itemWords: string[] = [];
    if (measurement.prefix != null) {
      itemWords.push(measurement.prefix);
    }
    itemWords.push(measurement.ingredient);
    if (measurement.suffix != null) {
      itemWords.push(measurement.suffix);
    }
    const itemText = itemWords.join(" ");

    const amountHtml = `<span class="amount">${escapeHtml(amountText)}</span>`;
    const itemHtml = `<span class="ingredient-text">${amountHtml} ${escapeHtml(itemText)}</span>`;
    htmlLines.push(
      '                    <li class="ingredient"><label>',
      '                        <input type="checkbox">',
      `                        ${itemHtml}`,
      "                    </label></li>",
    );
  }

  htmlLines.push(
    "                </ul>",
    "            </section>",
    '            <div class="method">',
  );

  if (recipe.notes != null) {
    htmlLines.push(
      '                <section class="notes">',
      "                    <h2>Notes</h2>",
      '                    <ul class="note-list">',
    );
    for (const note of recipe.notes) {
      htmlLines.push(`                        <li>${escapeHtml(note)}</li>`);
    }
    htmlLines.push("                    </ul>", "                </section>");
  }

  htmlLines.push(
    '                <section class="instructions">',
    "                    <h2>Instructions</h2>",
    '                    <ol class="step-list">',
  );
  for (const instruction of recipe.instructions) {
    htmlLines.push(`                        <li>${escapeHtml(instruction)}</li>`);
  }
  htmlLines.push(
    "                    </ol>",
    "                </section>",
    "            </div>",
    "        </div>",
    "    </main>",
    '    <footer class="site-footer">',
    "        <p>CoMo Recipes</p>",
    "    </footer>",
    "</body>",
    "</html>",
  );

  return htmlLines.join("\n") + "\n";
}

rmSync(distDir, { recursive: true, force: true });
mkdirSync(join(distDir, "formatted_recipes"), { recursive: true });
mkdirSync(join(distDir, "manifests"), { recursive: true });

// Shared static assets (stylesheet and favicon) for GitHub pages
cpSync(join(docsDir, "assets"), join(distDir, "assets"), { recursive: true });

// All formatted HTML recipes for GitHub pages
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

// Index file for GitHub pages
let totalRecipeCount = 0;
for (const relativePathToRecipeName of alphabetizedRelativePathToRecipeName.values()) {
  totalRecipeCount += relativePathToRecipeName.size;
}
const searchInputHtml =
  '<input id="recipe-search" type="search" placeholder="Search recipes" aria-label="Search recipes">';

const indexLines = [
  "<!DOCTYPE html>",
  '<html lang="en">',
  "<head>",
  '    <meta charset="UTF-8">',
  '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
  "    <title>CoMo Recipes</title>",
  '    <link rel="icon" href="assets/como_icon.ico">',
  '    <link rel="stylesheet" href="assets/style.css">',
  "</head>",
  '<body class="index-page">',
  '    <header class="site-header">',
  "        <h1>CoMo Recipes</h1>",
  `        <p class="tagline">Our household cookbook &middot; ${totalRecipeCount} recipes</p>`,
  '        <div class="search-bar">',
  `            ${searchInputHtml}`,
  "        </div>",
  "    </header>",
  '    <nav class="letter-nav">',
];
for (const startingLetter of alphabetizedRelativePathToRecipeName.keys()) {
  indexLines.push(`        <a href="#letter-${startingLetter}">${startingLetter}</a>`);
}
indexLines.push("    </nav>", '    <main class="index-grid">');
for (const [startingLetter, relativePathToRecipeName] of alphabetizedRelativePathToRecipeName) {
  indexLines.push(
    `        <section class="letter-section" id="letter-${startingLetter}">`,
    `            <h2>${startingLetter}</h2>`,
    "            <ul>",
  );
  for (const [relativePath, recipeName] of relativePathToRecipeName) {
    indexLines.push(`                <li><a href="${relativePath}">${escapeHtml(recipeName)}</a></li>`);
  }
  indexLines.push("            </ul>", "        </section>");
}
indexLines.push(
  "    </main>",
  '    <p class="no-results" hidden>No recipes match your search.</p>',
  '    <footer class="site-footer">',
  "        <p>CoMo Recipes</p>",
  "    </footer>",
  "    <script>",
  "        const searchInput = document.getElementById('recipe-search');",
  "        const letterNav = document.querySelector('.letter-nav');",
  "        const noResults = document.querySelector('.no-results');",
  "        const sections = Array.from(document.querySelectorAll('.letter-section'));",
  "        searchInput.addEventListener('input', () => {",
  "            const query = searchInput.value.trim().toLowerCase();",
  "            let anyMatches = false;",
  "            for (const section of sections) {",
  "                let sectionMatches = false;",
  "                for (const item of section.querySelectorAll('li')) {",
  "                    const matches = item.textContent.toLowerCase().includes(query);",
  "                    item.hidden = !matches;",
  "                    sectionMatches = sectionMatches || matches;",
  "                }",
  "                section.hidden = !sectionMatches;",
  "                anyMatches = anyMatches || sectionMatches;",
  "            }",
  "            letterNav.hidden = query !== '';",
  "            noResults.hidden = anyMatches;",
  "        });",
  "    </script>",
  "</body>",
  "</html>",
);
writeFileSync(join(distDir, "index.html"), indexLines.join("\n") + "\n");

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

// An empty .nojekyll file tells GitHub Pages to skip Jekyll entirely.
writeFileSync(join(distDir, ".nojekyll"), "");

console.log("Site built into dist/");
