import collections
import json
import pathlib

import como_recipes


def test_recipe_counts_consistency():
    docs_folder_path = pathlib.Path(__file__).parent.parent.parent / "docs"
    yaml_recipe_folder_path = docs_folder_path / "recipes"
    html_recipe_folder_path = docs_folder_path / "formatted_recipes"

    yaml_recipe_count = len(list(yaml_recipe_folder_path.glob(pattern="*.yaml")))
    html_recipe_count = len(list(html_recipe_folder_path.glob(pattern="*.html")))

    assert yaml_recipe_count == html_recipe_count


def test_units_consistent_per_ingredient():
    docs_folder_path = pathlib.Path(__file__).parent.parent.parent / "docs"
    yaml_recipe_folder_path = docs_folder_path / "recipes"

    recipes = [
        como_recipes.Recipe.from_yaml(file_path=file_path)
        for file_path in yaml_recipe_folder_path.glob(pattern="*.yaml")
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
    docs_folder_path = pathlib.Path(__file__).parent.parent.parent / "docs"
    yaml_recipe_folder_path = docs_folder_path / "recipes"

    recipes = [
        como_recipes.Recipe.from_yaml(file_path=file_path)
        for file_path in yaml_recipe_folder_path.glob(pattern="*.yaml")
    ]
    tags_per_recipe = {recipe.name: recipe.tags for recipe in recipes}

    duplicated_tags = {
        recipe_name: tags for recipe_name, tags in tags_per_recipe.items() if len(set(tags)) != len(tags)
    }
    message = f"\n\nRepeated tags found: \n{json.dumps(obj=duplicated_tags, indent=2)}\n"
    assert not any(duplicated_tags), message
