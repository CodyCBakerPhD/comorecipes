from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class WhippedCreamCheeseFilling(Recipe):
    name: str = "Whipped Cream Cheese Filling"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="", ingredient_name="cup heavy cream"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="", ingredient_name="cup powdered sugar"),
        IngredientRegistry.get_measurement(amount=3, unit="", ingredient_name="oz cream cheese"),
        IngredientRegistry.get_measurement(amount=1, unit="", ingredient_name="tsp vanilla extract"),
    )
    instructions: tuple[str, ...] = (
        "Chill whisk and bowl for stand mixer.",
        "Add all ingredients at once and mix on high until stiff peaks form.",
    )


default_recipe_registry.add_recipe(recipe=WhippedCreamCheeseFilling())
