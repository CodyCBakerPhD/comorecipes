from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class EnchiladaBeef(Recipe):
    name: str = "Enchilada Beef"
    tags: tuple[str, ...] = ("Mexican",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=24, unit="oz.", name="chuck roast"),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp.", name="flour"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", name="extra virgin olive oil"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="black pepper"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", name="water"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", name="beef concentrate"),
    )
    instructions: tuple[str, ...] = (
        "Dredge meat in flour and pepper. Brown in skillet.",
        "Heat water to simmer, add beef concentrate.",
        "Combine in crockpot, set to high for 1 hour. Turn to low for 6-7 hours.",
    )


default_recipe_registry.add_recipe(recipe=EnchiladaBeef())
