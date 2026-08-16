// Assembles the deployable site into dist/ (TypeScript port of the Python
// `generate_html_recipes` CLI — byte-for-byte identical output):
//   1. renders docs/recipes/*.yaml into styled dist/formatted_recipes/*.html,
//   2. generates the alphabetized dist/index.html with live search, tag filters, and list mode,
//   3. generates dist/shopping_list.html, which totals the ingredients of the recipes picked in list mode,
//   4. copies the shared stylesheet, theme script, favicon, and logo from docs/assets into dist/assets,
//   5. generates the dist/manifests/ database manifests and their hashes,
//   6. copies the raw recipe/ingredient databases,
//   7. adds .nojekyll so GitHub Pages serves the files verbatim (no Jekyll).
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

// The GitHub "mark" octicon, inlined so pages have no external image dependencies
const GITHUB_ICON_PATH =
  "M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49" +
  "-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58" +
  " 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59" +
  ".82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27" +
  " 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65" +
  " 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8" +
  "c0-4.42-3.58-8-8-8z";
const GITHUB_ICON_SVG = `<svg viewBox="0 0 16 16" aria-hidden="true"><path d="${GITHUB_ICON_PATH}"/></svg>`;
const GITHUB_REPOSITORY_URL = "https://github.com/CodyCBakerPhD/como_recipes";

const GITHUB_LINK_HTML =
  `<a class="icon-link" href="${GITHUB_REPOSITORY_URL}" aria-label="View source on GitHub">${GITHUB_ICON_SVG}</a>`;

const THEME_TOGGLE_HTML =
  '<button class="theme-toggle" type="button" onclick="comoToggleTheme()" aria-label="Toggle color theme"></button>';

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
function renderRecipeHtml(recipe: RawRecipe, tagToHue: Map<string, number>): string {
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
    '    <script src="../assets/theme.js"></script>',
    "</head>",
    '<body class="recipe-page">',
    '    <nav class="top-bar">',
    '        <a class="brand" href="../index.html">',
    '            <img class="brand-logo" src="../assets/como_logo.jpg" alt="CoMo logo">',
    "            <span>CoMo Recipes</span>",
    "        </a>",
    '        <div class="top-actions">',
    '            <a class="back-link" href="../index.html">&larr; Recipe Index</a>',
    `            ${THEME_TOGGLE_HTML}`,
    `            ${GITHUB_LINK_HTML}`,
    "        </div>",
    "    </nav>",
    '    <main class="recipe">',
    '        <header class="recipe-header">',
    `            <h1>${escapedName}</h1>`,
  ];

  if (recipe.tags != null) {
    htmlLines.push('            <ul class="tag-list">');
    for (const tag of recipe.tags) {
      const tagHue = tagToHue.get(tag) ?? 0;
      const tagLink = `<a href="../index.html?tag=${encodeURIComponent(tag)}">${escapeHtml(tag)}</a>`;
      htmlLines.push(`                <li class="tag" style="--tag-hue: ${tagHue}">${tagLink}</li>`);
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
    "</body>",
    "</html>",
  );

  return htmlLines.join("\n") + "\n";
}

// A recipe reduced to what the shopping list needs: an amount per unit, the prep
// qualifiers worth carrying to the store, and nothing else.
interface ShoppingItem {
  amount: number | null; // null for "enough", which has no measurable amount to total
  unit: string;
  ingredient: string;
  qualifier?: string;
}

interface ShoppingRecipe {
  name: string;
  items: ShoppingItem[];
}

function toShoppingRecipe(recipe: RawRecipe): ShoppingRecipe {
  const items = recipe.measurements.map((measurement) => {
    const parsedAmount = Number(measurement.amount);
    const qualifierWords = [
      measurement.prefix,
      // Suffixes are written as continuations of the ingredient, e.g. ", room temperature"
      measurement.suffix?.replace(/^,\s*/, ""),
    ].filter((word) => word != null && word !== "");

    const item: ShoppingItem = {
      amount: Number.isFinite(parsedAmount) ? parsedAmount : null,
      unit: getRenderedUnits(measurement),
      ingredient: measurement.ingredient,
    };
    if (qualifierWords.length > 0) {
      item.qualifier = qualifierWords.join(", ");
    }
    return item;
  });

  return { name: recipe.name, items };
}

// Inlined into a <script type="application/json"> block, so no "<" may survive verbatim.
function toEmbeddedJson(value: unknown): string {
  return JSON.stringify(value).replaceAll("<", "\\u003c");
}

function renderShoppingListHtml(shoppingRecipeByFileStem: Map<string, ShoppingRecipe>): string {
  const embeddedRecipes = toEmbeddedJson(Object.fromEntries(shoppingRecipeByFileStem));

  return [
    "<!DOCTYPE html>",
    '<html lang="en">',
    "<head>",
    '    <meta charset="UTF-8">',
    '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
    "    <title>Shopping List · CoMo Recipes</title>",
    '    <link rel="icon" href="assets/como_icon.ico">',
    '    <link rel="stylesheet" href="assets/style.css">',
    '    <script src="assets/theme.js"></script>',
    "</head>",
    '<body class="shopping-page">',
    '    <nav class="top-bar">',
    '        <a class="brand" href="index.html">',
    '            <img class="brand-logo" src="assets/como_logo.jpg" alt="CoMo logo">',
    "            <span>CoMo Recipes</span>",
    "        </a>",
    '        <div class="top-actions">',
    `            ${THEME_TOGGLE_HTML}`,
    `            ${GITHUB_LINK_HTML}`,
    "        </div>",
    "    </nav>",
    '    <main class="shopping">',
    '        <header class="shopping-header">',
    '            <div class="shopping-title">',
    "                <h1>Shopping List</h1>",
    '                <div class="shopping-actions">',
    '                    <a class="page-button edit-selection" href="index.html">&larr; Edit selection</a>',
    '                    <button class="page-button" type="button" onclick="window.print()">Print list</button>',
    "                </div>",
    "            </div>",
    '            <p class="tagline" id="list-summary"></p>',
    '            <ul class="recipe-chips" id="recipe-chips"></ul>',
    "        </header>",
    '        <section class="ingredients shopping-card">',
    "            <h2>Ingredients</h2>",
    '            <ul class="ingredient-list" id="shopping-items"></ul>',
    "        </section>",
    '        <p class="empty-state" hidden>No recipes selected yet. Open <a href="index.html">the recipe index</a>, switch on List Mode, and pick a few.</p>',
    "    </main>",
    `    <script type="application/json" id="recipe-data">${embeddedRecipes}</script>`,
    '    <script src="assets/shopping_list.js"></script>',
    "</body>",
    "</html>",
  ].join("\n") + "\n";
}

rmSync(distDir, { recursive: true, force: true });
mkdirSync(join(distDir, "formatted_recipes"), { recursive: true });
mkdirSync(join(distDir, "manifests"), { recursive: true });

// Shared static assets (stylesheet, theme script, favicon, and logo) for GitHub pages
cpSync(join(docsDir, "assets"), join(distDir, "assets"), { recursive: true });

// All formatted HTML recipes for GitHub pages
const recipesDir = join(docsDir, "recipes");
const fileStemToRecipe = new Map<string, RawRecipe>();
for (const fileStem of yamlStems(recipesDir)) {
  fileStemToRecipe.set(fileStem, loadYaml<RawRecipe>(join(recipesDir, `${fileStem}.yaml`)));
}

// Hues are spread evenly over the alphabetized tag universe so every tag chip gets a distinct color
const allTags = [...new Set([...fileStemToRecipe.values()].flatMap((recipe) => recipe.tags ?? []))].sort();
const totalTagCount = allTags.length;
const tagToHue = new Map<string, number>(allTags.map((tag, index) => [tag, Math.floor((index * 360) / totalTagCount)]));

const alphabetizedRelativePathToRecipe = new Map<string, Map<string, RawRecipe>>();
for (const [fileStem, recipe] of fileStemToRecipe) {
  const startingLetter = recipe.name[0].toUpperCase();

  const relativeHtmlPath = `formatted_recipes/${fileStem}.html`;
  let relativePathToRecipe = alphabetizedRelativePathToRecipe.get(startingLetter);
  if (relativePathToRecipe == null) {
    relativePathToRecipe = new Map<string, RawRecipe>();
    alphabetizedRelativePathToRecipe.set(startingLetter, relativePathToRecipe);
  }
  relativePathToRecipe.set(relativeHtmlPath, recipe);

  writeFileSync(join(distDir, relativeHtmlPath), renderRecipeHtml(recipe, tagToHue));
}

// Index file for GitHub pages
let totalRecipeCount = 0;
for (const relativePathToRecipe of alphabetizedRelativePathToRecipe.values()) {
  totalRecipeCount += relativePathToRecipe.size;
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
  '    <script src="assets/theme.js"></script>',
  '    <script defer src="assets/list_mode.js"></script>',
  "</head>",
  '<body class="index-page">',
  '    <nav class="top-bar">',
  '        <button class="list-mode-toggle" id="list-mode-toggle" type="button" aria-pressed="false">List Mode</button>',
  '        <div class="top-actions">',
  `            ${THEME_TOGGLE_HTML}`,
  `            ${GITHUB_LINK_HTML}`,
  "        </div>",
  "    </nav>",
  '    <header class="site-header">',
  '        <img class="site-logo" src="assets/como_logo.jpg" alt="CoMo logo">',
  "        <h1>CoMo Recipes</h1>",
  `        <p class="tagline">Our household cookbook &middot; ${totalRecipeCount} recipes</p>`,
  '        <div class="search-bar">',
  `            ${searchInputHtml}`,
  "        </div>",
  '        <div class="tag-filter">',
];
for (const tag of allTags) {
  const tagHue = tagToHue.get(tag) ?? 0;
  const escapedTag = escapeHtml(tag);
  const tagButton = `<button class="tag" type="button" style="--tag-hue: ${tagHue}" data-tag="${escapedTag}">`;
  indexLines.push(`            ${tagButton}${escapedTag}</button>`);
}
indexLines.push(
  "        </div>",
  "    </header>",
  '    <nav class="letter-nav">',
);
for (const startingLetter of alphabetizedRelativePathToRecipe.keys()) {
  indexLines.push(`        <a href="#letter-${startingLetter}">${startingLetter}</a>`);
}
indexLines.push("    </nav>", '    <main class="index-grid">');
for (const [startingLetter, relativePathToRecipe] of alphabetizedRelativePathToRecipe) {
  indexLines.push(
    `        <section class="letter-section" id="letter-${startingLetter}">`,
    `            <h2>${startingLetter}</h2>`,
    "            <ul>",
  );
  for (const [relativePath, recipe] of relativePathToRecipe) {
    const escapedTags = escapeHtml((recipe.tags ?? []).join(","));
    const recipeLink = `<a href="${relativePath}">${escapeHtml(recipe.name)}</a>`;
    indexLines.push(`                <li data-tags="${escapedTags}">${recipeLink}</li>`);
  }
  indexLines.push("            </ul>", "        </section>");
}
indexLines.push(
  "    </main>",
  '    <p class="no-results" hidden>No recipes match your search.</p>',
  '    <div class="selection-bar" hidden>',
  '        <p class="selection-count">0 recipes selected</p>',
  '        <div class="selection-actions">',
  '            <button class="selection-button clear-selection" type="button">Clear</button>',
  '            <a class="selection-button build-list" href="shopping_list.html" aria-disabled="true">Build Shopping List</a>',
  "        </div>",
  "    </div>",
  "    <script>",
  "        const searchInput = document.getElementById('recipe-search');",
  "        const letterNav = document.querySelector('.letter-nav');",
  "        const noResults = document.querySelector('.no-results');",
  "        const sections = Array.from(document.querySelectorAll('.letter-section'));",
  "        const tagButtons = Array.from(document.querySelectorAll('.tag-filter .tag'));",
  "        const selectedTags = new Set();",
  "        const applyFilters = () => {",
  "            const query = searchInput.value.trim().toLowerCase();",
  "            let anyMatches = false;",
  "            for (const section of sections) {",
  "                let sectionMatches = false;",
  "                for (const item of section.querySelectorAll('li')) {",
  "                    const itemTags = (item.dataset.tags || '').split(',');",
  "                    const matchesQuery = item.textContent.toLowerCase().includes(query);",
  "                    const matchesTags = [...selectedTags].every((tag) => itemTags.includes(tag));",
  "                    const matches = matchesQuery && matchesTags;",
  "                    item.hidden = !matches;",
  "                    sectionMatches = sectionMatches || matches;",
  "                }",
  "                section.hidden = !sectionMatches;",
  "                anyMatches = anyMatches || sectionMatches;",
  "            }",
  "            letterNav.hidden = query !== '' || selectedTags.size > 0;",
  "            noResults.hidden = anyMatches;",
  "        };",
  "        searchInput.addEventListener('input', applyFilters);",
  "        for (const button of tagButtons) {",
  "            button.addEventListener('click', () => {",
  "                const tag = button.dataset.tag;",
  "                if (selectedTags.has(tag)) {",
  "                    selectedTags.delete(tag);",
  "                } else {",
  "                    selectedTags.add(tag);",
  "                }",
  "                button.classList.toggle('selected');",
  "                applyFilters();",
  "            });",
  "        }",
  "        for (const tag of new URLSearchParams(location.search).getAll('tag')) {",
  "            const button = tagButtons.find((candidate) => candidate.dataset.tag === tag);",
  "            if (button != null) {",
  "                selectedTags.add(tag);",
  "                button.classList.add('selected');",
  "            }",
  "        }",
  "        if (selectedTags.size > 0) {",
  "            applyFilters();",
  "        }",
  "    </script>",
  "</body>",
  "</html>",
);
writeFileSync(join(distDir, "index.html"), indexLines.join("\n") + "\n");

// Shopping list page: list mode on the index links here with the chosen recipes in the query string
const shoppingRecipeByFileStem = new Map<string, ShoppingRecipe>();
for (const [fileStem, recipe] of fileStemToRecipe) {
  shoppingRecipeByFileStem.set(fileStem, toShoppingRecipe(recipe));
}
writeFileSync(join(distDir, "shopping_list.html"), renderShoppingListHtml(shoppingRecipeByFileStem));

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
