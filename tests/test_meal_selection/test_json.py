import como_recipes
from como_recipes import IngredientRegistry, MealSelection


def test_meal_selection_in_memory_json_roundtrip():
    meal_selection = MealSelection()

    new_meal = como_recipes.Meal()
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    new_meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    meal_selection.add_meal(meal=new_meal)

    measurement_1 = IngredientRegistry.get_measurement(amount=1.0, unit="g", ingredient_name="test_ingredient")
    meal_selection.add_measurement(measurement=measurement_1)
    measurement_2 = IngredientRegistry.get_measurement(amount=1.0, unit="tsp", ingredient_name="test_ingredient")
    meal_selection.remove_measurement(measurement=measurement_2)

    dictionary = meal_selection.to_json_dictionary()
    meal_selection_loaded = MealSelection.from_json_dictionary(dictionary=dictionary)

    assert meal_selection_loaded == meal_selection
