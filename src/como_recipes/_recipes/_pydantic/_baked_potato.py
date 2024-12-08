from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class BakedPotato(Recipe):
    name: str = "Baked Potato"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=4, unit="Good", name="big potatoes"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", name="olive oil"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="large-grain salt"),
    )
    instructions: tuple[str, ...] = (
        "Use aluminum foil for easy cleanup.",
        "Thoroughly scrub potatoes.",
        "Cut into quarters lengthwise.",
        "Rub all over with peanut oil and coat with a bit of large-grain salt.",
        "Bake for 45 min at 425 F.",
    )


default_recipe_registry.add_recipe(recipe=BakedPotato())
