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

Pushes to `main` here rebuild and publish the site to the `gh-pages` branch, and a daily scheduled run does the same to pick up changes to the database. Run the "Deploy site to gh-pages" workflow by hand from the Actions tab to publish a database change sooner. Pull requests get a preview deployment. Every build checks out the database repo's `main` branch, and trusts its records: the database repo validates them against its schemas before they can land there.
