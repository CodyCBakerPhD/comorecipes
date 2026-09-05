// The recipe data models: the shapes of the YAML database, how it is loaded, and the
// few derived views the pages need. Nothing in here knows about HTML.

import { readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

import { parse } from "yaml";

export interface Measurement {
  amount: string | number;
  unit?: string;
  prefix?: string;
  suffix?: string;
  ingredient: string;
}

export interface Recipe {
  name: string;
  tags?: string[];
  measurements: Measurement[];
  instructions: string[];
  notes?: string[];
}

export interface Ingredient {
  name: string;
  portions_text?: string;
}

// The sub-databases, each a directory of one YAML file per entry.
export const DATABASE_NAMES = ["recipes", "ingredients"] as const;

export interface Database {
  // File stem (the entry's id) to entry, alphabetized by stem
  recipes: Map<string, Recipe>;
  ingredients: Map<string, Ingredient>;
  // Every tag used by any recipe, alphabetized
  tags: string[];
}

export function yamlStems(directory: string): string[] {
  return readdirSync(directory)
    .filter((fileName) => fileName.endsWith(".yaml"))
    .map((fileName) => fileName.slice(0, -".yaml".length))
    .sort();
}

function loadEntries<Entry>(directory: string): Map<string, Entry> {
  const entries = new Map<string, Entry>();
  for (const stem of yamlStems(directory)) {
    entries.set(stem, parse(readFileSync(join(directory, `${stem}.yaml`), "utf-8")) as Entry);
  }
  return entries;
}

export function loadDatabase(databaseDir: string): Database {
  const recipes = loadEntries<Recipe>(join(databaseDir, "recipes"));
  const ingredients = loadEntries<Ingredient>(join(databaseDir, "ingredients"));
  const tags = [...new Set([...recipes.values()].flatMap((recipe) => recipe.tags ?? []))].sort();
  return { recipes, ingredients, tags };
}

// The unit as it should read on the page: registered ingredients spell out their own
// "portions" (e.g. "cloves" for garlic), and "enough" has no unit at all.
export function displayUnit(measurement: Measurement, database: Database): string {
  if (measurement.amount === "enough") {
    return "";
  }
  if (measurement.unit === "portions") {
    for (const ingredient of database.ingredients.values()) {
      if (ingredient.name === measurement.ingredient && ingredient.portions_text != null) {
        return ingredient.portions_text;
      }
    }
  }
  return measurement.unit ?? "";
}

// A recipe reduced to what the shopping list needs: an amount per unit, the prep
// qualifiers worth carrying to the store, and nothing else.
export interface ShoppingItem {
  amount: number | null; // null for "enough", which has no measurable amount to total
  unit: string;
  ingredient: string;
  qualifier?: string;
}

export interface ShoppingRecipe {
  name: string;
  items: ShoppingItem[];
}

export function toShoppingRecipe(recipe: Recipe, database: Database): ShoppingRecipe {
  const items = recipe.measurements.map((measurement) => {
    const parsedAmount = Number(measurement.amount);
    const qualifierWords = [
      measurement.prefix,
      // Suffixes are written as continuations of the ingredient, e.g. ", room temperature"
      measurement.suffix?.replace(/^,\s*/, ""),
    ].filter((word) => word != null && word !== "");

    const item: ShoppingItem = {
      amount: Number.isFinite(parsedAmount) ? parsedAmount : null,
      unit: displayUnit(measurement, database),
      ingredient: measurement.ingredient,
    };
    if (qualifierWords.length > 0) {
      item.qualifier = qualifierWords.join(", ");
    }
    return item;
  });

  return { name: recipe.name, items };
}
