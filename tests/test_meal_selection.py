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

    new_meal_selection = MealSelection()

    assert len(new_meal_selection) == 0
    assert repr(new_meal_selection) == "0 registered measurements\n"
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(new_meal_selection)
    assert captured_output.getvalue() == "0 registered measurements\n\n"

    new_meal_selection.add_measurement(measurement=example_measurement)

    expected_repr = "1 registered measurements\n-------------------------\n\nExample Ingredient 1\n  56 grams\n"
    assert len(new_meal_selection) == 1
    assert repr(new_meal_selection) == expected_repr
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(new_meal_selection)
    assert captured_output.getvalue() == expected_repr + "\n"

    expected_shopping_list = "Example Ingredient 1\n  56 grams\n"
    assert new_meal_selection.get_shopping_list() == expected_shopping_list

    new_meal_selection.add_recipe(recipe=recipe)

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
    assert len(new_meal_selection) == 3
    assert repr(new_meal_selection) == expected_repr
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(new_meal_selection)
    assert captured_output.getvalue() == expected_repr + "\n"

    new_meal_selection.add_measurement(measurement=example_measurement)

    expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\ningredient 2\n  4 g\n"
    assert new_meal_selection.get_shopping_list() == expected_shopping_list

    new_meal_selection.remove_measurement(
        measurement=IngredientRegistry.get_measurement(amount=2.0, unit="g", name="ingredient 2"),
    )

    expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\ningredient 2\n  2 g\n"
    assert new_meal_selection.get_shopping_list() == expected_shopping_list

    # Recipe should now be removed entirely from printout
    new_meal_selection.remove_measurement(
        measurement=IngredientRegistry.get_measurement(amount=2.0, unit="g", name="ingredient 2"),
    )

    expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\n"
    assert new_meal_selection.get_shopping_list() == expected_shopping_list

    expected_recipe_names = ["Example Recipe 1"]
    assert expected_recipe_names == new_meal_selection.get_all_recipe_names()

    new_meal_selection.remove_recipe(recipe_name="Example Recipe 1")

    expected_shopping_list = "Example Ingredient 1\n  112 grams\n"
    assert new_meal_selection.get_shopping_list() == expected_shopping_list


def test_get_shopping_list_error():
    meal_selection = MealSelection()

    measurement_1 = IngredientRegistry.get_measurement(amount=1.0, unit="g", name="test_ingredient")
    meal_selection.add_measurement(measurement=measurement_1)
    measurement_2 = IngredientRegistry.get_measurement(amount=1.0, unit="tsp", name="test_ingredient")
    meal_selection.add_measurement(measurement=measurement_2)

    expected_message = "\nMultiple units found for ingredient 'test_ingredient':\n\n[\n  1 g\n  1 tsp\n]"
    with pytest.raises(ValueError, match=re.escape(pattern=expected_message)):
        meal_selection.get_shopping_list()


def test_get_shopping_list_warning():
    meal_selection = MealSelection()

    measurement_1 = IngredientRegistry.get_measurement(amount=1.0, unit="g", name="test_ingredient")
    meal_selection.add_measurement(measurement=measurement_1)

    measurement_2 = IngredientRegistry.get_measurement(amount=2.0, unit="g", name="test_ingredient")
    meal_selection.remove_measurement(measurement=measurement_2)

    expected_message = "Negative amount of 'test_ingredient' found in shopping list; ignoring."
    with pytest.warns(UserWarning, match=expected_message):
        meal_selection.get_shopping_list()
