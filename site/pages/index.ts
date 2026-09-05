// The alphabetized recipe index with live search, tag filters, and list mode.

import type { Database, Recipe } from "../models.ts";
import { escapeHtml, pageHtml, tagHue } from "./layout.ts";

function recipeItemHtml(fileStem: string, recipe: Recipe): string {
  const tags = escapeHtml((recipe.tags ?? []).join(","));
  return `<li data-tags="${tags}"><a href="formatted_recipes/${fileStem}.html">${escapeHtml(recipe.name)}</a></li>`;
}

// Recipes grouped by the first letter of their name, in the database's alphabetical order
function groupByLetter(database: Database): Map<string, string[]> {
  const itemsByLetter = new Map<string, string[]>();
  for (const [fileStem, recipe] of database.recipes) {
    const letter = recipe.name[0].toUpperCase();
    const items = itemsByLetter.get(letter) ?? [];
    items.push(recipeItemHtml(fileStem, recipe));
    itemsByLetter.set(letter, items);
  }
  return itemsByLetter;
}

export function renderIndexPage(database: Database): string {
  const itemsByLetter = groupByLetter(database);

  const tagButtons = database.tags.map((tag) => {
    const escapedTag = escapeHtml(tag);
    return `<button class="tag" type="button" style="--tag-hue: ${tagHue(tag, database)}" data-tag="${escapedTag}">${escapedTag}</button>`;
  });
  const letterLinks = [...itemsByLetter.keys()].map((letter) => `<a href="#letter-${letter}">${letter}</a>`);
  const letterSections = [...itemsByLetter].map(
    ([letter, items]) => `<section class="letter-section" id="letter-${letter}">
            <h2>${letter}</h2>
            <ul>
                ${items.join("\n                ")}
            </ul>
        </section>`,
  );

  return pageHtml({
    title: "CoMo Recipes",
    bodyClass: "index-page",
    scripts: ['<script defer src="assets/search.js"></script>', '<script defer src="assets/list_mode.js"></script>'],
    topBarLead:
      '<button class="list-mode-toggle" id="list-mode-toggle" type="button" aria-pressed="false">List Mode</button>',
    body: `    <header class="site-header">
        <img class="site-logo" src="assets/como_logo.jpg" alt="CoMo logo">
        <h1>CoMo Recipes</h1>
        <p class="tagline">Our household cookbook &middot; ${database.recipes.size} recipes</p>
        <div class="search-bar">
            <input id="recipe-search" type="search" placeholder="Search recipes" aria-label="Search recipes">
        </div>
        <div class="tag-filter">
            ${tagButtons.join("\n            ")}
        </div>
    </header>
    <nav class="letter-nav">
        ${letterLinks.join("\n        ")}
    </nav>
    <main class="index-grid">
        ${letterSections.join("\n        ")}
    </main>
    <p class="no-results" hidden>No recipes match your search.</p>
    <div class="selection-bar" hidden>
        <p class="selection-count">0 recipes selected</p>
        <div class="selection-actions">
            <button class="selection-button clear-selection" type="button">Clear</button>
            <a class="selection-button build-list" href="shopping_list.html" aria-disabled="true">Build Shopping List</a>
        </div>
    </div>`,
  });
}
