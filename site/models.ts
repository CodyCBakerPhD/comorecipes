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
  // File stem of the recipe this ingredient is made from, when it is one ("marinara sauce"
  // in Spaghetti). Links are always declared here, never inferred from the ingredient name.
  recipe?: string;
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
  // Recipe stem to the stem of the recipe each of its measurements calls for, by measurement
  // index; only measurements whose ingredient is itself a recipe have an entry
  componentRecipes: Map<string, Map<number, string>>;
  // Recipe stem to the stems of the recipes that use it as an ingredient, in stem order
  usedIn: Map<string, string[]>;
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

// The recipe a measurement declares it is made from, checked against the database
function componentRecipeStem(
  fileStem: string,
  measurement: Measurement,
  recipes: Map<string, Recipe>,
): string | undefined {
  if (measurement.recipe == null) {
    return undefined;
  }
  if (!recipes.has(measurement.recipe)) {
    throw new Error(
      `Recipe "${fileStem}" says its ingredient "${measurement.ingredient}" is made from the recipe ` +
        `"${measurement.recipe}", but no such recipe exists in the database.`,
    );
  }
  if (measurement.recipe === fileStem) {
    throw new Error(`Recipe "${fileStem}" says its ingredient "${measurement.ingredient}" is made from itself.`);
  }
  return measurement.recipe;
}

// The cross-links between recipes: which measurements are other recipes, and the reverse
function linkRecipes(recipes: Map<string, Recipe>): Pick<Database, "componentRecipes" | "usedIn"> {
  const componentRecipes = new Map<string, Map<number, string>>();
  const usedIn = new Map<string, string[]>();
  for (const [fileStem, recipe] of recipes) {
    const components = new Map<number, string>();
    recipe.measurements.forEach((measurement, index) => {
      const componentStem = componentRecipeStem(fileStem, measurement, recipes);
      if (componentStem == null) {
        return;
      }
      components.set(index, componentStem);
      const users = usedIn.get(componentStem) ?? [];
      if (!users.includes(fileStem)) {
        users.push(fileStem);
      }
      usedIn.set(componentStem, users);
    });
    if (components.size > 0) {
      componentRecipes.set(fileStem, components);
    }
  }
  return { componentRecipes, usedIn };
}

export function loadDatabase(databaseDir: string): Database {
  const recipes = loadEntries<Recipe>(join(databaseDir, "recipes"));
  const ingredients = loadEntries<Ingredient>(join(databaseDir, "ingredients"));
  const tags = [...new Set([...recipes.values()].flatMap((recipe) => recipe.tags ?? []))].sort();
  return { recipes, ingredients, tags, ...linkRecipes(recipes) };
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
