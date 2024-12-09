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
    expected_str = "\ncomo_recipes.MealSelection()\n\n"
    assert repr(meal_selection) == expected_repr
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str

    with pytest.raises(
        expected_exception=ValueError,
        match="No meals or measurements have been added to the meal selection.",
    ):
        meal_selection.get_shopping_list()

    with pytest.raises(
        expected_exception=ValueError,
        match="No meals or measurements have been added to the meal selection.",
    ):
        meal_selection.get_raw_measurement_list()

    # Test adding a meal
    new_meal = como_recipes.Meal()
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    meal_selection.add_meal(meal=new_meal)

    expected_repr = (
        "\n"
        "como_recipes.MealSelection(\n"
        "\t_meals={\n"
        "\t\t('Aglio E Olio', 'Sauteed Green Beans'): como_recipes.Meal(...),\n"
        "\t},\n"
        ")\n"
    )
    assert repr(meal_selection) == expected_repr

    expected_str = "\n1 selected meal\n---------------\n\nAglio E Olio, Sauteed Green Beans\n\n"
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str

    expected_raw_ingredient_list = [
        "Raw Ingredient List",
        "-------------------",
        "☐  cloves of garlic",
        "\t8 large",
        "☐  crushed red pepper",
        "\t2 tsp.",
        "☐  fresh Parmesan",
        "\t1 cup",
        "☐  fresh green beans",
        "\t1 bag",
        "☐  olive oil",
        "\t1/3 cup",
        "\t1 enough",
        "☐  parsley",
        "\t1/4 cup",
        "☐  salt",
        "\t1 tbsp.",
        "☐  salt & pepper",
        "\t1 enough",
        "☐  thin spaghetti",
        "\t1 lb.",
        "☐  water",
        "\t2 qt.",
    ]
    assert meal_selection.get_raw_measurement_list() == expected_raw_ingredient_list

    # TODO
    # expected_shopping_list = ""
    # assert meal_selection.get_shopping_list() == expected_shopping_list

    # Test adding a measurement
    meal_selection.add_measurement(measurement=example_measurement)

    expected_repr = (
        "\n"
        "como_recipes.MealSelection(\n"
        "\t_meals={\n"
        "\t\t('Aglio E Olio', 'Sauteed Green Beans'): como_recipes.Meal(...),\n"
        "\t},\n"
        "\t_individual_measurements_to_add={\n"
        '\t\t"Example Ingredient 1": [\n'
        '\t\t\tMeasurement(amount=56, unit="grams", '
        'ingredient=Ingredient(name="Example Ingredient 1", '
        'default_grams_per_package=12.34, default_package_unit="container")),\n'
        "\t\t],\n"
        "\t},\n"
        ")\n"
    )
    assert repr(meal_selection) == expected_repr

    expected_str = (
        "\n"
        "1 selected meal\n"
        "---------------\n"
        "\n"
        "Aglio E Olio, Sauteed Green Beans\n"
        "\n"
        "\n"
        "1 added measurement\n"
        "-------------------\n"
        "\n"
        "Example Ingredient 1\n"
        "\n"
    )
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str

    expected_raw_ingredient_list = [
        "Raw Ingredient List",
        "-------------------",
        "☐  Example Ingredient 1",
        "\t56 grams",
        "☐  cloves of garlic",
        "\t8 large",
        "☐  crushed red pepper",
        "\t2 tsp.",
        "☐  fresh Parmesan",
        "\t1 cup",
        "☐  fresh green beans",
        "\t1 bag",
        "☐  olive oil",
        "\t1/3 cup",
        "\t1 enough",
        "☐  parsley",
        "\t1/4 cup",
        "☐  salt",
        "\t1 tbsp.",
        "☐  salt & pepper",
        "\t1 enough",
        "☐  thin spaghetti",
        "\t1 lb.",
        "☐  water",
        "\t2 qt.",
    ]
    assert meal_selection.get_raw_measurement_list() == expected_raw_ingredient_list

    # TODO
    # expected_shopping_list = ""
    # assert meal_selection.get_shopping_list() == expected_shopping_list

    # Test removing less of the same measurement
    meal_selection.remove_measurement(
        measurement=IngredientRegistry.get_measurement(amount=0.5, unit="g", ingredient_name="Example Ingredient 1"),
    )

    expected_repr = (
        "\n"
        "como_recipes.MealSelection(\n"
        "\t_meals={\n"
        "\t\t('Aglio E Olio', 'Sauteed Green Beans'): como_recipes.Meal(...),\n"
        "\t},\n"
        "\t_individual_measurements_to_add={\n"
        '\t\t"Example Ingredient 1": [\n'
        '\t\t\tMeasurement(amount=56, unit="grams", '
        'ingredient=Ingredient(name="Example Ingredient 1", '
        'default_grams_per_package=12.34, default_package_unit="container")),\n'
        "\t\t],\n"
        "\t},\n"
        "\t_individual_measurements_to_remove={\n"
        '\t\t"Example Ingredient 1": [\n'
        '\t\t\tMeasurement(amount=1/2, unit="g", ingredient=Ingredient(name="Example '
        'Ingredient 1")),\n'
        "\t\t],\n"
        "\t},\n"
        ")\n"
    )
    assert repr(meal_selection) == expected_repr

    expected_str = (
        "\n"
        "1 selected meal\n"
        "---------------\n"
        "\n"
        "Aglio E Olio, Sauteed Green Beans\n"
        "\n"
        "\n"
        "1 added measurement\n"
        "-------------------\n"
        "\n"
        "Example Ingredient 1\n"
        "\n"
        "\n"
        "1 removed measurement\n"
        "---------------------\n"
        "\n"
        "Example Ingredient 1\n"
        "\n"
    )
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str

    expected_raw_ingredient_list = [
        "Raw Ingredient List",
        "-------------------",
        "☐  Example Ingredient 1",
        "\t56 grams",
        "☐  cloves of garlic",
        "\t8 large",
        "☐  crushed red pepper",
        "\t2 tsp.",
        "☐  fresh Parmesan",
        "\t1 cup",
        "☐  fresh green beans",
        "\t1 bag",
        "☐  olive oil",
        "\t1/3 cup",
        "\t1 enough",
        "☐  parsley",
        "\t1/4 cup",
        "☐  salt",
        "\t1 tbsp.",
        "☐  salt & pepper",
        "\t1 enough",
        "☐  thin spaghetti",
        "\t1 lb.",
        "☐  water",
        "\t2 qt.",
    ]
    assert meal_selection.get_raw_measurement_list() == expected_raw_ingredient_list

    # TODO
    # expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\n"
    # assert meal_selection.get_shopping_list() == expected_shopping_list

    # Test removing all of what remains of that same measurement
    meal_selection.remove_measurement(
        measurement=IngredientRegistry.get_measurement(amount=0.5, unit="g", ingredient_name="Example Ingredient 1"),
    )

    expected_repr = (
        "\n"
        "como_recipes.MealSelection(\n"
        "\t_meals={\n"
        "\t\t('Aglio E Olio', 'Sauteed Green Beans'): como_recipes.Meal(...),\n"
        "\t},\n"
        "\t_individual_measurements_to_add={\n"
        '\t\t"Example Ingredient 1": [\n'
        '\t\t\tMeasurement(amount=56, unit="grams", '
        'ingredient=Ingredient(name="Example Ingredient 1", '
        'default_grams_per_package=12.34, default_package_unit="container")),\n'
        "\t\t],\n"
        "\t},\n"
        "\t_individual_measurements_to_remove={\n"
        '\t\t"Example Ingredient 1": [\n'
        '\t\t\tMeasurement(amount=1/2, unit="g", ingredient=Ingredient(name="Example '
        'Ingredient 1")),\n'
        '\t\t\tMeasurement(amount=1/2, unit="g", ingredient=Ingredient(name="Example '
        'Ingredient 1")),\n'
        "\t\t],\n"
        "\t},\n"
        ")\n"
    )
    assert repr(meal_selection) == expected_repr

    expected_str = (
        "\n"
        "1 selected meal\n"
        "---------------\n"
        "\n"
        "Aglio E Olio, Sauteed Green Beans\n"
        "\n"
        "\n"
        "1 added measurement\n"
        "-------------------\n"
        "\n"
        "Example Ingredient 1\n"
        "\n"
        "\n"
        "1 removed measurement\n"
        "---------------------\n"
        "\n"
        "Example Ingredient 1\n"
        "\n"
    )
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str

    expected_raw_ingredient_list = [
        "Raw Ingredient List",
        "-------------------",
        "☐  Example Ingredient 1",
        "\t56 grams",
        "☐  cloves of garlic",
        "\t8 large",
        "☐  crushed red pepper",
        "\t2 tsp.",
        "☐  fresh Parmesan",
        "\t1 cup",
        "☐  fresh green beans",
        "\t1 bag",
        "☐  olive oil",
        "\t1/3 cup",
        "\t1 enough",
        "☐  parsley",
        "\t1/4 cup",
        "☐  salt",
        "\t1 tbsp.",
        "☐  salt & pepper",
        "\t1 enough",
        "☐  thin spaghetti",
        "\t1 lb.",
        "☐  water",
        "\t2 qt.",
    ]
    assert meal_selection.get_raw_measurement_list() == expected_raw_ingredient_list

    # TODO
    # expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\n"
    # assert meal_selection.get_shopping_list() == expected_shopping_list

    # Test removing a meal
    meal_selection.remove_meal(recipe_names=("Aglio E Olio", "Sauteed Green Beans"))

    expected_repr = (
        "\n"
        "como_recipes.MealSelection(\n"
        "\t_individual_measurements_to_add={\n"
        '\t\t"Example Ingredient 1": [\n'
        '\t\t\tMeasurement(amount=56, unit="grams", '
        'ingredient=Ingredient(name="Example Ingredient 1", '
        'default_grams_per_package=12.34, default_package_unit="container")),\n'
        "\t\t],\n"
        "\t},\n"
        "\t_individual_measurements_to_remove={\n"
        '\t\t"Example Ingredient 1": [\n'
        '\t\t\tMeasurement(amount=1/2, unit="g", ingredient=Ingredient(name="Example '
        'Ingredient 1")),\n'
        '\t\t\tMeasurement(amount=1/2, unit="g", ingredient=Ingredient(name="Example '
        'Ingredient 1")),\n'
        "\t\t],\n"
        "\t},\n"
        ")\n"
    )
    assert repr(meal_selection) == expected_repr

    expected_str = (
        "\n"
        "1 added measurement\n"
        "-------------------\n"
        "\n"
        "Example Ingredient 1\n"
        "\n"
        "\n"
        "1 removed measurement\n"
        "---------------------\n"
        "\n"
        "Example Ingredient 1\n"
        "\n"
    )
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str

    expected_raw_ingredient_list = [
        "Raw Ingredient List",
        "-------------------",
        "☐  Example Ingredient 1",
        "\t56 grams",
    ]
    assert meal_selection.get_raw_measurement_list() == expected_raw_ingredient_list

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
