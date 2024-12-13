from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class SpaghettiSquash(Recipe):
    name: str = "Spaghetti Squash"
    tags: tuple[str, ...] = ("Italian", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="spaghetti", ingredient_name="squash"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="olive oil"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="salt and pepper"),
    )
    instructions: tuple[str, ...] = (
        "Cut and clean inside of squash.",
        "Coat with oil and season.",
        "Place face down on baking sheet lined with aluminum foil.",
        "Bake for 40 minutes at 375 F.",
    )


default_recipe_registry.add_recipe(recipe=SpaghettiSquash())
