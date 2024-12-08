from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class BananaBread(Recipe):
    name: str = "Banana Bread"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", name="butter"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="cup", name="sugar"),
        IngredientRegistry.get_measurement(amount=1, unit="large", name="egg"),
        IngredientRegistry.get_measurement(amount=1, unit="ripe", name="banana"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="tsp.", name="of salt"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="baking soda"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", name="flour"),
    )
    instructions: tuple[str, ...] = (
        "Preheat oven to 300 F.",
        "Cream butter and sugar.",
        "Combine all dry ingredients and mix well.",
        "Combine all remaining ingredients and mix well.",
        "Bake for 35 minutes.",
    )


default_recipe_registry.add_recipe(recipe=BananaBread())
