// One recipe: its tags, tickable ingredients, notes, numbered instructions, and the
// cross-links to the recipes it is made from and the recipes made from it.

import { displayUnit, type Database, type Measurement, type Recipe } from "../models.ts";
import { escapeHtml, pageHtml, tagHue } from "./layout.ts";

// Units the page leaves unwritten, either because there is none or because the
// amount already reads naturally without it (e.g. "1 thin spaghetti").
const UNWRITTEN_UNITS = new Set(["", "portions"]);

// Recipe pages sit side by side in formatted_recipes/, so they link to each other by stem
function recipeLinkHtml(fileStem: string, text: string, database: Database): string {
  const recipe = database.recipes.get(fileStem);
  const title = recipe == null ? "" : ` title="${escapeHtml(recipe.name)}"`;
  return `<a class="recipe-link" href="${encodeURIComponent(fileStem)}.html"${title}>${escapeHtml(text)}</a>`;
}

// An ingredient that is itself a recipe links to that recipe's page; the prefix and suffix
// stay plain text, since they describe this recipe's use of it ("chilled rice").
function ingredientHtml(measurement: Measurement, componentStem: string | undefined, database: Database): string {
  const unit = displayUnit(measurement, database);
  const amountText = UNWRITTEN_UNITS.has(unit) ? `${measurement.amount}` : `${measurement.amount} ${unit}`;
  const nameHtml =
    componentStem == null
      ? escapeHtml(measurement.ingredient)
      : recipeLinkHtml(componentStem, measurement.ingredient, database);
  const itemHtml = [
    measurement.prefix == null ? null : escapeHtml(measurement.prefix),
    nameHtml,
    measurement.suffix == null ? null : escapeHtml(measurement.suffix),
  ]
    .filter((part) => part != null)
    .join(" ");

  return `<li class="ingredient"><label>
                        <input type="checkbox">
                        <span class="ingredient-text"><span class="amount">${escapeHtml(amountText)}</span> ${itemHtml}</span>
                    </label></li>`;
}

// The reverse links: every recipe that calls for this one as an ingredient
function usedInHtml(fileStem: string, database: Database): string {
  const userStems = database.usedIn.get(fileStem);
  if (userStems == null) {
    return "";
  }
  const userItems = userStems.map(
    (userStem) => `<li>${recipeLinkHtml(userStem, database.recipes.get(userStem)?.name ?? userStem, database)}</li>`,
  );
  return `
                <section class="used-in">
                    <h2>Used In</h2>
                    <ul class="used-in-list">
                        ${userItems.join("\n                        ")}
                    </ul>
                </section>`;
}

function tagListHtml(recipe: Recipe, database: Database): string {
  if (recipe.tags == null) {
    return "";
  }
  const tagItems = recipe.tags.map(
    (tag) =>
      `<li class="tag" style="--tag-hue: ${tagHue(tag, database)}">` +
      `<a href="../index.html?tag=${encodeURIComponent(tag)}">${escapeHtml(tag)}</a></li>`,
  );
  return `
            <ul class="tag-list">
                ${tagItems.join("\n                ")}
            </ul>`;
}

function notesHtml(recipe: Recipe): string {
  if (recipe.notes == null) {
    return "";
  }
  const noteItems = recipe.notes.map((note) => `<li>${escapeHtml(note)}</li>`);
  return `<section class="notes">
                    <h2>Notes</h2>
                    <ul class="note-list">
                        ${noteItems.join("\n                        ")}
                    </ul>
                </section>
                `;
}

export function renderRecipePage(fileStem: string, recipe: Recipe, database: Database): string {
  const componentStems = database.componentRecipes.get(fileStem);
  const ingredientItems = recipe.measurements.map((measurement, index) =>
    ingredientHtml(measurement, componentStems?.get(index), database),
  );
  const instructionItems = recipe.instructions.map((instruction) => `<li>${escapeHtml(instruction)}</li>`);

  return pageHtml({
    title: `${recipe.name} · CoMo Recipes`,
    bodyClass: "recipe-page",
    rootPath: "../",
    topBarActions: ['<a class="back-link" href="../index.html">&larr; Recipe Index</a>'],
    body: `    <main class="recipe">
        <header class="recipe-header">
            <h1>${escapeHtml(recipe.name)}</h1>${tagListHtml(recipe, database)}
        </header>
        <div class="recipe-body">
            <section class="ingredients">
                <h2>Ingredients</h2>
                <ul class="ingredient-list">
                    ${ingredientItems.join("\n                    ")}
                </ul>
            </section>
            <div class="method">
                ${notesHtml(recipe)}<section class="instructions">
                    <h2>Instructions</h2>
                    <ol class="step-list">
                        ${instructionItems.join("\n                        ")}
                    </ol>
                </section>${usedInHtml(fileStem, database)}
            </div>
        </div>
    </main>`,
  });
}
