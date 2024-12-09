from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class MochiDonuts(Recipe):
    name: str = "Mochi Donuts"
    tags: tuple[str, ...] = ("Dessert", "Breakfast")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=150, unit="grams", ingredient_name="mochiko"),
        IngredientRegistry.get_measurement(amount=50, unit="grams", ingredient_name="brown sugar"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp", ingredient_name="baking powder"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=50, unit="grams", ingredient_name="melted butter"),
        IngredientRegistry.get_measurement(amount=1, unit="large", ingredient_name="egg"),
        IngredientRegistry.get_measurement(amount=200, unit="grams", ingredient_name="whole milk"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp", ingredient_name="vanilla"),
    )
    instructions: tuple[str, ...] = (
        "Preheat to 350. grease pan.",
        "Combine dry ingredients, whisk together.",
        "Combine wet ingredients.",
        "Combine dry and wet ingredients until smooth.",
        "Bake for 25-30 minutes.",
        "Let cool for 5-10 minutes before icing.",
    )


default_recipe_registry.add_recipe(recipe=MochiDonuts())
