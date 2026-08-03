# CoMo Recipes

Static website for our household's recipe collection, built from the recipe/ingredient YAML database with a
TypeScript site generator (`npm run build`, see `scripts/build.ts`).

The Python meal planning app, its tests, and the source-of-truth recipe/ingredient database now live in the
[`recipes`](https://github.com/CodyCBakerPhD/recipes) repository. This repo keeps a synced copy of the YAML content
under `docs/recipes` and `docs/ingredients` so the site can keep building from it.

## Installation

To install and run the app, use the [CoMo Launcher](https://github.com/CodyCBakerPhD/como_apps_launcher_public/releases).
