// One recipe: its tags, tickable ingredients, notes, and numbered instructions.

import { displayUnit, type Database, type Measurement, type Recipe } from "../models.ts";
import { escapeHtml, pageHtml, tagHue } from "./layout.ts";

// Units the page leaves unwritten, either because there is none or because the
// amount already reads naturally without it (e.g. "1 thin spaghetti").
const UNWRITTEN_UNITS = new Set(["", "portions"]);

function ingredientHtml(measurement: Measurement, database: Database): string {
  const unit = displayUnit(measurement, database);
  const amountText = UNWRITTEN_UNITS.has(unit) ? `${measurement.amount}` : `${measurement.amount} ${unit}`;
  const itemText = [measurement.prefix, measurement.ingredient, measurement.suffix]
    .filter((word) => word != null)
    .join(" ");

  return `<li class="ingredient"><label>
                        <input type="checkbox">
                        <span class="ingredient-text"><span class="amount">${escapeHtml(amountText)}</span> ${escapeHtml(itemText)}</span>
                    </label></li>`;
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

export function renderRecipePage(recipe: Recipe, database: Database): string {
  const ingredientItems = recipe.measurements.map((measurement) => ingredientHtml(measurement, database));
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
                </section>
            </div>
        </div>
    </main>`,
  });
}
