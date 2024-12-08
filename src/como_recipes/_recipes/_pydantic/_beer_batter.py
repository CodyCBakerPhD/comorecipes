from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class BeerBatter(Recipe):
    name: str = "Beer Batter"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=2, unit="cups", name="flour"),
        IngredientRegistry.get_measurement(amount=1 / 3, unit="cup", name="cornstarch"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp.", name="salt"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", name="paprika"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", name="baking powder"),
        IngredientRegistry.get_measurement(amount=12, unit="oz.", name="beer"),
    )
    instructions: tuple[str, ...] = (
        "Whisk dry ingredients. Add beer and incorporate. Mixture should feel like pancake batter.",
        "Cook 2-3 minutes per side in 375 F oil.",
    )


default_recipe_registry.add_recipe(recipe=BeerBatter())
