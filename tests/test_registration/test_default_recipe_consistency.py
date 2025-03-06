import collections
import json
import pathlib

import como_recipes


def test_recipe_counts_consistency():
    docs_folder_path = pathlib.Path(__file__).parent.parent.parent / "docs"
    yaml_recipe_folder_path = docs_folder_path / "recipes"
    html_recipe_folder_path = docs_folder_path / "formatted_recipes"

    default_recipe_count = len(como_recipes.default_recipe_registry.get_all_recipe_names())
    yaml_recipe_count = len(list(yaml_recipe_folder_path.glob(pattern="*.yaml")))
    html_recipe_count = len(list(html_recipe_folder_path.glob(pattern="*.html")))

    assert yaml_recipe_count == default_recipe_count
    assert html_recipe_count == default_recipe_count


def test_units_consistent_per_ingredient():
    recipes = [
        como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name)
        for recipe_name in como_recipes.default_recipe_registry.get_all_recipe_names()
    ]

    all_ingredient_occurences_to_units = collections.defaultdict(list)
    for recipe in recipes:
        for measurement in recipe.measurements:
            if measurement.amount == "enough":
                continue

            all_ingredient_occurences_to_units[measurement.ingredient.name].append(measurement.unit)

    inconsistent_ingredients = {
        ingredient_name: tuple(unique_units)
        for ingredient_name, units in all_ingredient_occurences_to_units.items()
        if len(unique_units := set(units)) != 1
    }
    message = f"\n\nInconsistent units found: \n{json.dumps(obj=inconsistent_ingredients, indent=2)}\n"
    assert not any(inconsistent_ingredients), message


def test_no_repeated_tags():
    tags_per_recipe = {
        recipe_name: como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name).tags
        for recipe_name in como_recipes.default_recipe_registry.get_all_recipe_names()
    }

    duplicated_tags = {
        recipe_name: tags for recipe_name, tags in tags_per_recipe.items() if len(set(tags)) != len(tags)
    }
    message = f"\n\nRepeated tags found: \n{json.dumps(obj=duplicated_tags, indent=2)}\n"
    assert not any(duplicated_tags), message
