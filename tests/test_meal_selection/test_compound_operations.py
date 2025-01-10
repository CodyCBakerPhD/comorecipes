import io
import unittest.mock

import como_recipes
from como_recipes import IngredientRegistry, MealSelection, Measurement


def test_meal_selection_add_measurement_with_recipes(example_measurement: Measurement):
    meal_selection = MealSelection()

    new_meal = como_recipes.Meal()
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    meal_selection.add_meal(meal=new_meal)

    # Test adding a single individual measurement onto the previously tested recipes
    meal_selection.add_measurement(measurement=example_measurement)

    expected_repr = (
        "\n"
        "como_recipes.MealSelection(\n"
        "\t_meals={\n"
        "\t\t('Aglio E Olio', 'Sauteed Green Beans'): como_recipes.Meal(...),\n"
        "\t},\n"
        "\t_individual_measurements_to_add={\n"
        '\t\t"Example Ingredient 1": [\n'
        '\t\t\tMeasurement(amount=45, unit="grams", '
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
        "    45 grams",
        "☐  Parmesan",
        "    80 grams",
        "☐  crushed red pepper",
        "    2 grams",
        "☐  fresh green beans",
        "    1 portions",
        "☐  garlic",
        "    32 grams",
        "☐  olive oil",
        "    76 grams",
        "☐  salt",
        "    17 grams",
        "☐  thin spaghetti",
        "    1 portions",
        "☐  water",
        "    960 grams",
    ]
    assert meal_selection.get_raw_measurement_list() == expected_raw_ingredient_list

    # TODO
    # expected_shopping_list = ""
    # assert meal_selection.get_shopping_list() == expected_shopping_list


def test_meal_selection_remove_measurement_after_adding_with_recipes(example_measurement: Measurement):
    meal_selection = MealSelection()

    new_meal = como_recipes.Meal()
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    meal_selection.add_meal(meal=new_meal)

    meal_selection.add_measurement(measurement=example_measurement)

    # Test removing less of the same individual measurement
    meal_selection.remove_measurement(
        measurement=IngredientRegistry.get_measurement(
            amount=0.5,
            unit=example_measurement.unit,
            ingredient_name=example_measurement.ingredient.name,
        ),
    )

    expected_repr = (
        "\n"
        "como_recipes.MealSelection(\n"
        "\t_meals={\n"
        "\t\t('Aglio E Olio', 'Sauteed Green Beans'): como_recipes.Meal(...),\n"
        "\t},\n"
        "\t_individual_measurements_to_add={\n"
        '\t\t"Example Ingredient 1": [\n'
        '\t\t\tMeasurement(amount=45, unit="grams", '
        'ingredient=Ingredient(name="Example Ingredient 1", '
        'default_grams_per_package=12.34, default_package_unit="container")),\n'
        "\t\t],\n"
        "\t},\n"
        "\t_individual_measurements_to_remove={\n"
        '\t\t"Example Ingredient 1": [\n'
        '\t\t\tMeasurement(amount=0.5, unit="grams", ingredient=Ingredient(name="Example '
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
        "    45 grams",
        "☐  Parmesan",
        "    80 grams",
        "☐  crushed red pepper",
        "    2 grams",
        "☐  fresh green beans",
        "    1 portions",
        "☐  garlic",
        "    32 grams",
        "☐  olive oil",
        "    76 grams",
        "☐  salt",
        "    17 grams",
        "☐  thin spaghetti",
        "    1 portions",
        "☐  water",
        "    960 grams",
    ]
    assert meal_selection.get_raw_measurement_list() == expected_raw_ingredient_list

    # TODO
    # expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\n"
    # assert meal_selection.get_shopping_list() == expected_shopping_list


def test_meal_selection_remove_all_measurement_after_adding_with_recipes(example_measurement: Measurement):
    meal_selection = MealSelection()

    new_meal = como_recipes.Meal()
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    meal_selection.add_meal(meal=new_meal)

    meal_selection.add_measurement(measurement=example_measurement)

    # Test removing the entire amount of the same individual measurement
    meal_selection.remove_measurement(
        measurement=IngredientRegistry.get_measurement(
            amount=example_measurement.amount,
            unit=example_measurement.unit,
            ingredient_name=example_measurement.ingredient.name,
        ),
    )

    expected_repr = (
        "\n"
        "como_recipes.MealSelection(\n"
        "\t_meals={\n"
        "\t\t('Aglio E Olio', 'Sauteed Green Beans'): como_recipes.Meal(...),\n"
        "\t},\n"
        "\t_individual_measurements_to_add={\n"
        '\t\t"Example Ingredient 1": [\n'
        '\t\t\tMeasurement(amount=45, unit="grams", '
        'ingredient=Ingredient(name="Example Ingredient 1", '
        'default_grams_per_package=12.34, default_package_unit="container")),\n'
        "\t\t],\n"
        "\t},\n"
        "\t_individual_measurements_to_remove={\n"
        '\t\t"Example Ingredient 1": [\n'
        '\t\t\tMeasurement(amount=45, unit="grams", '
        'ingredient=Ingredient(name="Example Ingredient 1")),\n'
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
        "    45 grams",
        "☐  Parmesan",
        "    80 grams",
        "☐  crushed red pepper",
        "    2 grams",
        "☐  fresh green beans",
        "    1 portions",
        "☐  garlic",
        "    32 grams",
        "☐  olive oil",
        "    76 grams",
        "☐  salt",
        "    17 grams",
        "☐  thin spaghetti",
        "    1 portions",
        "☐  water",
        "    960 grams",
    ]
    assert meal_selection.get_raw_measurement_list() == expected_raw_ingredient_list

    # TODO
    # expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\n"
    # assert meal_selection.get_shopping_list() == expected_shopping_list
