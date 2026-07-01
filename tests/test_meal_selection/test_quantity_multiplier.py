import io
import unittest.mock

import como_recipes


def test_meal_selection_add_meal_repr():
    meal_selection = como_recipes.MealSelection()

    new_meal = como_recipes.Meal(quantity_multiplier=3.5)
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    meal_selection.add_meal(meal=new_meal)

    expected_repr = (
        "\n"
        "como_recipes.MealSelection(\n"
        "\t_meals={\n"
        "\t\t('Aglio E Olio', 'Sauteed Green Beans'): "
        "como_recipes.Meal(quantity_multiplier=3.5, ...),\n"
        "\t},\n"
        ")\n"
    )
    assert repr(meal_selection) == expected_repr


def test_meal_selection_add_meal_print():
    meal_selection = como_recipes.MealSelection()

    new_meal = como_recipes.Meal(quantity_multiplier=3.5)
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    meal_selection.add_meal(meal=new_meal)

    expected_str = "\n1 selected meal\n---------------\n\nAglio E Olio, Sauteed Green Beans\n\n"
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str


def test_meal_selection_add_meal_get_raw_ingredient_list():
    meal_selection = como_recipes.MealSelection()

    new_meal = como_recipes.Meal(quantity_multiplier=3.5)
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    meal_selection.add_meal(meal=new_meal)

    expected_raw_ingredient_list = [
        "Raw Ingredient List",
        "-------------------",
        "☐  Parmesan",
        "    280.0 grams",
        "☐  crushed red pepper",
        "    7.0 grams",
        "☐  garlic",
        "    112.0 grams",
        "☐  green beans",
        "    3150.0 grams",
        "☐  olive oil",
        "    266.0 grams",
        "☐  salt",
        "    59.5 grams",
        "☐  thin spaghetti",
        "    3.5 portions",
        "☐  water",
        "    6370.0 grams",
    ]
    assert meal_selection.get_raw_measurement_list() == expected_raw_ingredient_list


def test_meal_selection_add_meal_get_shopping_list():
    meal_selection = como_recipes.MealSelection()

    new_meal = como_recipes.Meal(quantity_multiplier=3.5)
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    meal_selection.add_meal(meal=new_meal)

    expected_shopping_list = {
        "Parmesan": (280.0, "grams"),
        "crushed red pepper": (7.0, "grams"),
        "garlic": (3, "heads"),
        "green beans": (3150.0, "grams"),
        "olive oil": (266.0, "grams"),
        "salt": (59.5, "grams"),
        "thin spaghetti": (4, "(16 oz.) packages"),
    }
    assert meal_selection.get_shopping_list() == expected_shopping_list
