from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class SpanishRice(Recipe):
    name: str = "Spanish Rice"
    tags: tuple[str, ...] = ("Mexican",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", name="butter"),
        IngredientRegistry.get_measurement(amount=1, unit="shallot", name=""),
        IngredientRegistry.get_measurement(amount=2, unit="cloves", name="garlic"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", name="long grain brown rice"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", name="salt and pepper"),
        IngredientRegistry.get_measurement(amount=5 / 2, unit="cups", name="not-chicken broth"),
        IngredientRegistry.get_measurement(amount=2, unit="sprigs", name="of thyme"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", name="parsley"),
    )
    instructions: tuple[str, ...] = (
        "Melt butter over medium heat. Add shallot and garlic, saute until tender.",
        "Add rice and stir until glossy. Add stock and herbs, bring to boil.",
        "Reduce to low or simmer and let cook for 30-40 minutes until all liquid is gone.",
        "Note: Rinse the rice beforehand to make fluffier",
    )


default_recipe_registry.add_recipe(recipe=SpanishRice())
