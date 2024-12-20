from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class ChocolateCake(Recipe):
    name: str = "Chocolate Cake"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian", "Chocolate")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=8, unit="grams", ingredient_name="flour"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=3 / 8, unit="cup", ingredient_name="cocoa powder"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp", ingredient_name="baking powder"),
        IngredientRegistry.get_measurement(amount=3 / 4, unit="tsp", ingredient_name="baking soda"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", ingredient_name="espresso powder"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="milk"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="vegetable oil"),
        IngredientRegistry.get_measurement(amount=1, unit="large", ingredient_name="egg"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp", ingredient_name="vanilla"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="boiling water"),
    )
    instructions: tuple[str, ...] = (
        "Preheat to 350 F. Spray pan.",
        "Add all dry ingredients and mix. Boil water.",
        "Add non-water wet ingredients and mix until well combined. Reduce speed and carefully add boiling water and mix well.",
        "Immediately transfer mixture to pan and bake for 30-35 minutes.",
    )


default_recipe_registry.add_recipe(recipe=ChocolateCake())
