from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class BechamelSauce(Recipe):
    name: str = "Bechamel Sauce"
    tags: tuple[str, ...] = ("European",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", name="butter"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", name="flour"),
        IngredientRegistry.get_measurement(amount=5 / 4, unit="cup", name="whole milk"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="salt and pepper"),
    )
    instructions: tuple[str, ...] = ("Make roux with butter and flour. Thicken with milk. Season.",)


default_recipe_registry.add_recipe(recipe=BechamelSauce())
