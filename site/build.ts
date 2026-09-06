// Assembles the deployable site into dist/ from the recipe database:
//   1. loads the database checkout into typed models (site/models.ts),
//   2. renders each recipe page, the index, and the shopping list (site/pages/),
//   3. copies the shared assets from site/assets,
//   4. publishes the raw database with manifests, which the desktop app syncs from,
//   5. adds .nojekyll so GitHub Pages serves the files verbatim.
//
// The database lives in its own repo (https://github.com/CodyCBakerPhD/comorecipes-database),
// which validates every record against its schemas before merging, so the build trusts them.
// The build reads it from DATABASE_DIR when set, otherwise from a database/ checkout at the
// root of this repo (gitignored; the workflows check it out there).
//
// Run with `npm run build` (requires Node >= 22.18 for native type stripping).

import { createHash } from "node:crypto";
import { cpSync, existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

import { DATABASE_NAMES, loadDatabase, yamlStems } from "./models.ts";
import { renderIndexPage } from "./pages/index.ts";
import { renderRecipePage } from "./pages/recipe.ts";
import { renderShoppingListPage } from "./pages/shopping_list.ts";

const repoRoot = dirname(dirname(fileURLToPath(import.meta.url)));
const databaseDir = resolve(process.env.DATABASE_DIR || join(repoRoot, "database"));
const siteDir = join(repoRoot, "site");
const distDir = join(repoRoot, "dist");

function md5(content: Buffer | string): string {
  return createHash("md5").update(content).digest("hex");
}

for (const databaseName of DATABASE_NAMES) {
  if (!existsSync(join(databaseDir, databaseName))) {
    throw new Error(
      `No recipe database found at ${databaseDir} (missing ${databaseName}/). Clone ` +
        "https://github.com/CodyCBakerPhD/comorecipes-database to database/ at the root of " +
        "this repo, or set DATABASE_DIR to an existing checkout.",
    );
  }
}

const database = loadDatabase(databaseDir);

rmSync(distDir, { recursive: true, force: true });
mkdirSync(join(distDir, "formatted_recipes"), { recursive: true });
mkdirSync(join(distDir, "manifests"), { recursive: true });

// Pages
for (const [fileStem, recipe] of database.recipes) {
  writeFileSync(join(distDir, "formatted_recipes", `${fileStem}.html`), renderRecipePage(fileStem, recipe, database));
}
writeFileSync(join(distDir, "index.html"), renderIndexPage(database));
writeFileSync(join(distDir, "shopping_list.html"), renderShoppingListPage(database));

// Shared stylesheet, scripts, favicon, and logo
cpSync(join(siteDir, "assets"), join(distDir, "assets"), { recursive: true });

// The raw database (just the YAML, not the READMEs beside it) and its manifests, which the
// desktop app compares against its local copy
for (const databaseName of DATABASE_NAMES) {
  const sourceDir = join(databaseDir, databaseName);
  const stems = yamlStems(sourceDir);
  mkdirSync(join(distDir, databaseName), { recursive: true });
  for (const fileStem of stems) {
    cpSync(join(sourceDir, `${fileStem}.yaml`), join(distDir, databaseName, `${fileStem}.yaml`));
  }

  const manifest = stems
    .map((fileStem) => `${fileStem}: ${md5(readFileSync(join(sourceDir, `${fileStem}.yaml`)))}\n`)
    .join("");
  writeFileSync(join(distDir, "manifests", `${databaseName}.yaml`), manifest);
  writeFileSync(join(distDir, "manifests", `${databaseName}_hash.txt`), `${md5(manifest)}\n`);
}

writeFileSync(join(distDir, ".nojekyll"), "");

console.log(`Site built into dist/ (${database.recipes.size} recipes)`);
