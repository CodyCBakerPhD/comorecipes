from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class KeyLimeFilling(Recipe):
    name: str = "Key Lime Filling"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=28, unit="oz.", ingredient_name="sweetened condensed milk"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="sour cream"),
        IngredientRegistry.get_measurement(amount=3 / 4, unit="cup", ingredient_name="Key lime juice"),
    )
    instructions: tuple[str, ...] = (
        "Mix.",
        "Eat as pudding by dipping Graham crackers in it, or bake in Graham cracker crust for about 10 minutes at 350 F.",
    )


default_recipe_registry.add_recipe(recipe=KeyLimeFilling())
