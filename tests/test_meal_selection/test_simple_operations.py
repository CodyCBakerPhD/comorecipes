import io
import unittest.mock

import como_recipes
from como_recipes import MealSelection


def test_meal_selection_add_meal_repr():
    meal_selection = MealSelection()

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


def test_meal_selection_add_meal_print():
    meal_selection = MealSelection()

    new_meal = como_recipes.Meal()
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    meal_selection.add_meal(meal=new_meal)

    expected_str = "\n1 selected meal\n---------------\n\nAglio E Olio, Sauteed Green Beans\n\n"
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str


def test_meal_selection_add_meal_get_raw_ingredient_list():
    meal_selection = MealSelection()

    new_meal = como_recipes.Meal()
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    meal_selection.add_meal(meal=new_meal)

    expected_raw_ingredient_list = [
        "Raw Ingredient List",
        "-------------------",
        "☐  Parmesan",
        "    80 grams",
        "☐  crushed red pepper",
        "    2 grams",
        "☐  garlic",
        "    32 grams",
        "☐  green beans",
        "    900 grams",
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


def test_meal_selection_add_meal_get_shopping_list():
    meal_selection = MealSelection()

    new_meal = como_recipes.Meal()
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    meal_selection.add_meal(meal=new_meal)

    expected_shopping_list = {
        "Parmesan": (80, "grams"),
        "crushed red pepper": (2, "grams"),
        "garlic": (1, "heads"),
        "green beans": (900, "grams"),
        "olive oil": (76, "grams"),
        "salt": (17, "grams"),
        "thin spaghetti": (1, "(16 oz.) packages"),
    }
    assert meal_selection.get_shopping_list() == expected_shopping_list


def test_meal_selection_add_meal_get_shopping_list_printout():
    meal_selection = MealSelection()

    new_meal = como_recipes.Meal()
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    meal_selection.add_meal(meal=new_meal)

    expected_shopping_list_printout = (
        "Meals\n"
        "-----\n"
        "\n"
        "\n"
        "☐ Aglio E Olio with Sauteed Green Beans\n"
        "\n"
        "\n"
        "\n"
        "\n"
        "Ingredients\n"
        "-----------\n"
        "\n"
        "\n"
        "☐  Parmesan               ☐  crushed red pepper     ☐  "
        "garlic                 \n"
        "    80 grams                  2 grams                   1 "
        "heads               \n"
        "☐  green beans            ☐  olive oil              ☐  "
        "salt                   \n"
        "    900 grams                 76 grams                  17 "
        "grams              \n"
        "☐  thin spaghetti         \n"
        "    1 (16 oz.) packages   "
    )
    assert meal_selection.get_shopping_list_printout() == expected_shopping_list_printout


def test_meal_selection_remove_meal():
    meal_selection = MealSelection()

    new_meal = como_recipes.Meal()
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    meal_selection.add_meal(meal=new_meal)

    meal_selection.remove_meal(recipe_names=("Aglio E Olio", "Sauteed Green Beans"))

    expected_repr = "\ncomo_recipes.MealSelection()\n"
    assert repr(meal_selection) == expected_repr

    expected_str = "\ncomo_recipes.MealSelection()\n\n"
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_str
