// The shopping list, which totals the ingredients of the recipes picked in list mode.
// Every recipe's measurements are embedded so the totalling happens client side.

import { toShoppingRecipe, type Database, type ShoppingRecipe } from "../models.ts";
import { pageHtml } from "./layout.ts";

// Inlined into a <script type="application/json"> block, so no "<" may survive verbatim.
function toEmbeddedJson(value: unknown): string {
  return JSON.stringify(value).replaceAll("<", "\\u003c");
}

export function renderShoppingListPage(database: Database): string {
  const shoppingRecipeByFileStem: Record<string, ShoppingRecipe> = {};
  for (const [fileStem, recipe] of database.recipes) {
    shoppingRecipeByFileStem[fileStem] = toShoppingRecipe(recipe, database);
  }

  return pageHtml({
    title: "Shopping List · CoMo Recipes",
    bodyClass: "shopping-page",
    body: `    <main class="shopping">
        <header class="shopping-header">
            <div class="shopping-title">
                <h1>Shopping List</h1>
                <div class="shopping-actions">
                    <a class="page-button edit-selection" href="index.html">&larr; Edit selection</a>
                    <button class="page-button" type="button" onclick="window.print()">Print list</button>
                </div>
            </div>
            <p class="tagline" id="list-summary"></p>
            <ul class="recipe-chips" id="recipe-chips"></ul>
        </header>
        <section class="ingredients shopping-card">
            <h2>Ingredients</h2>
            <ul class="ingredient-list" id="shopping-items"></ul>
        </section>
        <p class="empty-state" hidden>No recipes selected yet. Open <a href="index.html">the recipe index</a>, switch on List Mode, and pick a few.</p>
    </main>
    <script type="application/json" id="recipe-data">${toEmbeddedJson(shoppingRecipeByFileStem)}</script>
    <script src="assets/shopping_list.js"></script>`,
  });
}
