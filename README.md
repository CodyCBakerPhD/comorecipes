# CoMo Recipes

Static website for our household's recipe collection, built from the associated [recipe database](https://github.com/CodyCBakerPhD/comorecipes-database).

This repo holds only the site: the TypeScript build in `site/` and the deploy workflows. The recipes and ingredients themselves live in the database repo, and changes to them are made there.



## Building locally

The build reads the database from a `database/` checkout at the root of this repo (gitignored), or from wherever `DATABASE_DIR` points.

```sh
git clone https://github.com/CodyCBakerPhD/comorecipes-database database
npm ci
npm run build   # writes dist/
npm run serve   # serves dist/ locally
```



## Deploying

Pushes to `main` here, and pushes to `main` of the database repo, rebuild and publish the site to the `gh-pages` branch. Pull requests get a preview deployment. Both workflows check out the database repo's `main` branch, so the site always reflects the latest data.
