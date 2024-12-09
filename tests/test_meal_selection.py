import io
import pathlib
import re
import unittest.mock

import pytest

from como_recipes import IngredientRegistry, MealSelection, Measurement, Recipe


def test_meal_selection(example_measurement: Measurement):
    example_folder_path = pathlib.Path(__file__).parent / "examples" / "example_1"

    example_1_markdown_file_path = example_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    meal_selection = MealSelection()

    expected_repr = "\ncomo_recipes.MealSelection()\n"
    expected_str = "como_recipes.MealSelection with 0 selected meals or measurements\n\n"
    assert repr(meal_selection) == expected_repr
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str

    meal_selection.add_measurement(measurement=example_measurement)

    expected_repr = (
        "\n"
        "como_recipes.MealSelection(\n"
        "\t_individual_measurements_to_add={\n"
        "\t\tExample Ingredient 1: [\n"
        '\t\t\tMeasurement(amount=56, unit="grams", '
        'ingredient=Ingredient(name="Example Ingredient 1", '
        'default_grams_per_package=12.34, default_package_unit="container"))\n'
        "\t\t],\n"
        "\t},\n"
        ")\n"
    )
    expected_str = "1 added measurements\n---------------------\n\nExample Ingredient 1\n\n\n"
    assert repr(meal_selection) == expected_repr
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str

    # TODO
    # expected_shopping_list = "Example Ingredient 1\n  56 grams\n"
    # assert new_meal_selection.get_shopping_list() == expected_shopping_list

    meal_selection.add_recipe(recipe=recipe)

    expected_repr = (
        "3 registered measurements\n"
        "-------------------------\n"
        "\n"
        "Example Ingredient 1\n"
        "  56 grams\n"
        "ingredient 1\n"
        "  31/10 tbsp.\n"
        "ingredient 2\n"
        "  4 g\n"
    )
    assert repr(meal_selection) == expected_repr
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_repr + "\n"

    meal_selection.add_measurement(measurement=example_measurement)

    # TODO
    # expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\ningredient 2\n  4 g\n"
    # assert new_meal_selection.get_shopping_list() == expected_shopping_list

    meal_selection.remove_measurement(
        measurement=IngredientRegistry.get_measurement(amount=2.0, unit="g", ingredient_name="ingredient 2"),
    )

    # TODO
    # expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\ningredient 2\n  2 g\n"
    # assert new_meal_selection.get_shopping_list() == expected_shopping_list

    # Recipe should now be removed entirely from printout
    meal_selection.remove_measurement(
        measurement=IngredientRegistry.get_measurement(amount=2.0, unit="g", ingredient_name="ingredient 2"),
    )

    # TODO
    # expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\n"
    # assert new_meal_selection.get_shopping_list() == expected_shopping_list

    expected_recipe_names = ["Example Recipe 1"]
    assert expected_recipe_names == meal_selection.get_all_recipe_names()

    meal_selection.remove_recipe(recipe_name="Example Recipe 1")

    expected_shopping_list = "Example Ingredient 1\n  112 grams\n"
    assert meal_selection.get_shopping_list() == expected_shopping_list


def test_get_shopping_list_error():
    meal_selection = MealSelection()

    measurement_1 = IngredientRegistry.get_measurement(amount=1.0, unit="g", ingredient_name="test_ingredient")
    meal_selection.add_measurement(measurement=measurement_1)
    measurement_2 = IngredientRegistry.get_measurement(amount=1.0, unit="tsp", ingredient_name="test_ingredient")
    meal_selection.add_measurement(measurement=measurement_2)

    expected_message = "\nMultiple units found for ingredient 'test_ingredient':\n\n[\n  1 g\n  1 tsp\n]"
    with pytest.raises(ValueError, match=re.escape(pattern=expected_message)):
        meal_selection.get_shopping_list()


def test_get_shopping_list_warning():
    meal_selection = MealSelection()

    measurement_1 = IngredientRegistry.get_measurement(amount=1.0, unit="g", ingredient_name="test_ingredient")
    meal_selection.add_measurement(measurement=measurement_1)

    measurement_2 = IngredientRegistry.get_measurement(amount=2.0, unit="g", ingredient_name="test_ingredient")
    meal_selection.remove_measurement(measurement=measurement_2)

    expected_message = "Negative amount of 'test_ingredient' found in shopping list; ignoring."
    with pytest.warns(UserWarning, match=expected_message):
        meal_selection.get_shopping_list()
