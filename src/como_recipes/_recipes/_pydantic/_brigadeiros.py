from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class Brigadeiros(Recipe):
    name: str = "Brigadeiros"
    tags: tuple[str, ...] = ("Brazilian",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=3, unit="tbsp.", ingredient_name="unsweetened cocoa"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=14, unit="oz.", ingredient_name="condensed milk"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", ingredient_name="chocolate sprinkles"),
    )
    instructions: tuple[str, ...] = (
        "Combine cocoa, butter, and condensed milk in a medium saucepan over medium heat.",
        "Cook and stir until thickened, about 10 minutes.",
        "Remove from heat and let rest until just cool enough to handle.",
        "Form into small balls and coat with sprinkles.",
    )


default_recipe_registry.add_recipe(recipe=Brigadeiros())
