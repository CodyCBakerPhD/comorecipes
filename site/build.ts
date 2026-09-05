// Assembles the deployable site into dist/ from the recipe database:
//   1. loads database/ into typed models (site/models.ts),
//   2. renders each recipe page, the index, and the shopping list (site/pages/),
//   3. copies the shared assets from site/assets,
//   4. publishes the raw database with manifests, which the desktop app syncs from,
//   5. adds .nojekyll so GitHub Pages serves the files verbatim.
//
// Run with `npm run build` (requires Node >= 22.18 for native type stripping).

import { createHash } from "node:crypto";
import { cpSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

import { DATABASE_NAMES, loadDatabase, yamlStems } from "./models.ts";
import { renderIndexPage } from "./pages/index.ts";
import { renderRecipePage } from "./pages/recipe.ts";
import { renderShoppingListPage } from "./pages/shopping_list.ts";

const repoRoot = dirname(dirname(fileURLToPath(import.meta.url)));
const databaseDir = join(repoRoot, "database");
const siteDir = join(repoRoot, "site");
const distDir = join(repoRoot, "dist");

function md5(content: Buffer | string): string {
  return createHash("md5").update(content).digest("hex");
}

const database = loadDatabase(databaseDir);

rmSync(distDir, { recursive: true, force: true });
mkdirSync(join(distDir, "formatted_recipes"), { recursive: true });
mkdirSync(join(distDir, "manifests"), { recursive: true });

// Pages
for (const [fileStem, recipe] of database.recipes) {
  writeFileSync(join(distDir, "formatted_recipes", `${fileStem}.html`), renderRecipePage(recipe, database));
}
writeFileSync(join(distDir, "index.html"), renderIndexPage(database));
writeFileSync(join(distDir, "shopping_list.html"), renderShoppingListPage(database));

// Shared stylesheet, scripts, favicon, and logo
cpSync(join(siteDir, "assets"), join(distDir, "assets"), { recursive: true });

// The raw database and its manifests, which the desktop app compares against its local copy
for (const databaseName of DATABASE_NAMES) {
  const sourceDir = join(databaseDir, databaseName);
  cpSync(sourceDir, join(distDir, databaseName), { recursive: true });

  const manifest = yamlStems(sourceDir)
    .map((fileStem) => `${fileStem}: ${md5(readFileSync(join(sourceDir, `${fileStem}.yaml`)))}\n`)
    .join("");
  writeFileSync(join(distDir, "manifests", `${databaseName}.yaml`), manifest);
  writeFileSync(join(distDir, "manifests", `${databaseName}_hash.txt`), `${md5(manifest)}\n`);
}

writeFileSync(join(distDir, ".nojekyll"), "");

console.log(`Site built into dist/ (${database.recipes.size} recipes)`);
