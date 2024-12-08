from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class Rice(Recipe):
    name: str = "Rice"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=3 / 2, unit="cups", ingredient_name="rice"),
        IngredientRegistry.get_measurement(amount=2, unit="cups", ingredient_name="water"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="butter"),
    )
    instructions: tuple[str, ...] = (
        "Thoroughly rinse and pre-soak rice for 15 minutes.",
        "Add everything to a covered pot, bring to boil over medium-high heat (takes around 3 minutes).",
        "Immediately reduce to second lowest heat level for around 20 minutes.",
        "When water is evaporated, check rice to ensure it's not crunchy or soggy.",
    )


default_recipe_registry.add_recipe(recipe=Rice())
