from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class RoastPumpkin(Recipe):
    name: str = "Roast Pumpkin"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=5 / 2, unit="lb", ingredient_name="sugar pumpkin"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="coconut oil"),
    )
    instructions: tuple[str, ...] = (
        "Cut pumpkin in half length-wise. Scrape out seeds and string.",
        "Brush with oil and pierce outer skin a few times for steam to escape. Bake for 45-50 minutes at 350 F. Let cool and then scoop out meat.",
    )


default_recipe_registry.add_recipe(recipe=RoastPumpkin())
