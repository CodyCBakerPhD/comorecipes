from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class FryingBreading(Recipe):
    name: str = "Frying Breading"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=6, unit="cups", name="all-purpose flour"),
        IngredientRegistry.get_measurement(amount=10, unit="tbsp.", name="salt and pepper"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", name="garlic powder"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", name="onion powder"),
        IngredientRegistry.get_measurement(amount=4, unit="tsp.", name="cayenne pepper"),
    )
    instructions: tuple[str, ...] = ("Mix in large batches and store for later use.",)


default_recipe_registry.add_recipe(recipe=FryingBreading())
