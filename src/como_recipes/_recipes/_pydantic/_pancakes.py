from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class Pancakes(Recipe):
    name: str = "Pancakes"
    tags: tuple[str, ...] = ("American", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="", ingredient_name="cup flour"),
        IngredientRegistry.get_measurement(amount=2, unit="", ingredient_name="tbsp. sugar"),
        IngredientRegistry.get_measurement(amount=1, unit="", ingredient_name="tsp. baking powder"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="", ingredient_name="tsp. baking soda"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="", ingredient_name="tsp. salt"),
        IngredientRegistry.get_measurement(amount=1, unit="", ingredient_name="egg"),
        IngredientRegistry.get_measurement(amount=2, unit="", ingredient_name="tbsp. butter"),
        IngredientRegistry.get_measurement(amount=1, unit="", ingredient_name="cup buttermilk"),
    )
    instructions: tuple[str, ...] = (
        "Combine dry ingredients.",
        "Melt butter, mix with egg and buttermilk; whisk well.",
        "Cook on griddle.",
    )


default_recipe_registry.add_recipe(recipe=Pancakes())
