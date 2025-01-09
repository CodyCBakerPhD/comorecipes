import pathlib

import como_recipes


def test_recipe_counts_consistency():
    package_source_folder_path = pathlib.Path(__file__).parent.parent.parent / "src"
    yaml_recipe_folder_path = package_source_folder_path / "como_recipes" / "_recipes"
    html_recipe_folder_path = package_source_folder_path.parent / "docs" / "formatted_recipes"

    default_recipe_count = len(como_recipes.default_recipe_registry.get_all_recipe_names())
    markdown_recipe_count = len(list(yaml_recipe_folder_path.glob(pattern="*.yaml")))
    html_recipe_count = len(list(html_recipe_folder_path.glob(pattern="*.html")))

    assert markdown_recipe_count == default_recipe_count
    assert html_recipe_count == default_recipe_count


def test_all_units_consistent():
    recipes = [
        como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name)
        for recipe_name in como_recipes.default_recipe_registry.get_all_recipe_names()
    ]

    unique_units = {
        measurement.unit for recipe in recipes for measurement in recipe.measurements if measurement.amount != "enough"
    }

    assert unique_units == {"grams", "portions"}
