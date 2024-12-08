from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class NutellaBites(Recipe):
    name: str = "Nutella Bites"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=3 / 2, unit="", name="cups oats"),
        IngredientRegistry.get_measurement(amount=2 / 3, unit="", name="cup Nutella"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="", name="cu. shredded coconut"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="", name="cup honey"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="", name="cup roasted hazelnuts"),
        IngredientRegistry.get_measurement(amount=2, unit="", name="tsp. vanilla extract"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="", name="tsp. salt"),
    )
    instructions: tuple[str, ...] = (
        "Combine all ingredients in large bowl and mix thoroughly.",
        "Cover and put in refrigerator for 30-60 minutes to make texture easier to mold.",
        "Roll balls of desired size and keep refrigerated.",
    )


default_recipe_registry.add_recipe(recipe=NutellaBites())
