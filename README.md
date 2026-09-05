# CoMo Recipes

Static website for our household's recipe collection, built from the associated [recipe database](https://github.com/CodyCBakerPhD/recipes).

## Layout

The recipe data and the site that renders it are kept apart:

| Path | What it is |
|:--|:--|
| `database/recipes/` | One YAML file per recipe (synced copy of the upstream database) |
| `database/ingredients/` | One YAML file per registered ingredient |
| `database/README.md` | Conventions for the YAML content |
| `site/models.ts` | The recipe data models: YAML shapes, loading, and derived views |
| `site/pages/` | One renderer per page (recipe, index, shopping list) plus the shared layout |
| `site/assets/` | Stylesheet, client-side scripts, favicon, and logo |
| `site/build.ts` | Assembles everything into `dist/` |

`dist/` is the built site and is never committed. It also carries the raw database and its manifests, which the desktop app syncs from.

## Building

```bash
npm ci
npm run build   # renders the site into dist/
npm run serve   # serves dist/ locally
```

Pushes to `main` build and publish `dist/` to the `gh-pages` branch, and pull requests get a preview under `pr-preview/`.

## Updating recipes

The YAML under `database/` mirrors `docs/recipes` and `docs/ingredients` in the [recipes repository](https://github.com/CodyCBakerPhD/recipes), which is the source of truth. Copy changes over and the site rebuilds on the next push.
