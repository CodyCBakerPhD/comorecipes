import io
import re
import unittest.mock

import pytest

import como_recipes
from como_recipes import IngredientRegistry, MealSelection, Measurement


def test_meal_selection(example_measurement: Measurement):
    """A sequence of integration tests for the `MealSelection` class."""
    # Test an empty MealSelection
    meal_selection = MealSelection()

    expected_repr = "\ncomo_recipes.MealSelection()\n"
    expected_str = "como_recipes.MealSelection with 0 selected meals or measurements\n\n"
    assert repr(meal_selection) == expected_repr
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str

    # TODO
    expected_shopping_list = ""
    assert meal_selection.get_shopping_list() == expected_shopping_list

    # Test adding a meal
    new_meal = como_recipes.Meal()
    new_meal.add_default_recipe(recipe_name="Aglio E Olio")
    new_meal.add_default_recipe(recipe_name="Sauteed Green Beans")
    meal_selection.add_meal(meal=new_meal)

    expected_repr = (
        "\n"
        "como_recipes.MealSelection(\n"
        "\t_meals={\n"
        "\t\t('Aglio E Olio', 'Sauteed Green Beans'): como_recipes.Meal(...),\n"
        "\t},\n"
        ")\n"
    )
    expected_str = "1 selected meals\n-----------------\n\nAglio E Olio, Sauteed Green Beans\n\n\n"
    assert repr(meal_selection) == expected_repr
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str

    expected_shopping_list = ""
    assert meal_selection.get_shopping_list() == expected_shopping_list

    # Test adding a measurement
    meal_selection.add_measurement(measurement=example_measurement)

    expected_repr = (
        "\n"
        "como_recipes.MealSelection(\n"
        "\t_meals={\n"
        "\t\t('Aglio E Olio', 'Sauteed Green Beans'): como_recipes.Meal(...),\n"
        "\t},\n"
        "\t_individual_measurements_to_add={\n"
        "\t\tExample Ingredient 1: [\n"
        '\t\t\tMeasurement(amount=56, unit="grams", '
        'ingredient=Ingredient(name="Example Ingredient 1", '
        'default_grams_per_package=12.34, default_package_unit="container"))\n'
        "\t\t],\n"
        "\t},\n"
        ")\n"
    )
    expected_str = (
        "1 selected meals\n"
        "-----------------\n"
        "\n"
        "Aglio E Olio, Sauteed Green Beans\n"
        "\n"
        "1 added measurements\n"
        "---------------------\n"
        "\n"
        "Example Ingredient 1\n"
        "\n"
        "\n"
    )
    assert repr(meal_selection) == expected_repr
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str

    expected_shopping_list = ""
    assert meal_selection.get_shopping_list() == expected_shopping_list

    # Test removing less of the same measurement
    meal_selection.remove_measurement(
        measurement=IngredientRegistry.get_measurement(amount=0.5, unit="g", ingredient_name="Example Ingredient 1"),
    )

    expected_repr = ""
    expected_str = ""
    assert repr(meal_selection) == expected_repr
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str

    # TODO
    # expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\n"
    # assert meal_selection.get_shopping_list() == expected_shopping_list

    # Test removing all of what remains of that same measurement
    meal_selection.remove_measurement(
        measurement=IngredientRegistry.get_measurement(amount=0.5, unit="g", ingredient_name="Example Ingredient 1"),
    )

    expected_repr = ""
    expected_str = ""
    assert repr(meal_selection) == expected_repr
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str

    # TODO
    # expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\n"
    # assert meal_selection.get_shopping_list() == expected_shopping_list

    # Test removing a meal
    meal_selection.remove_meal(recipe_name="Example Recipe 1")

    expected_repr = ""
    expected_str = ""
    assert repr(meal_selection) == expected_repr
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str

    # TODO
    # expected_shopping_list = "Example Ingredient 1\n  112 grams\n"
    # assert meal_selection.get_shopping_list() == expected_shopping_list


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
