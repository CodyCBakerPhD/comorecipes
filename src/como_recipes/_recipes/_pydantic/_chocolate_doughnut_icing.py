from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class ChocolateDoughnutIcing(Recipe):
    name: str = "Chocolate Doughnut Icing"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=3 / 4, unit="cup", ingredient_name="powdered sugar"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", ingredient_name="dutch cocoa powder"),
        IngredientRegistry.get_measurement(amount=1 / 16, unit="tsp.", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", ingredient_name="milk"),
        IngredientRegistry.get_measurement(amount=3 / 4, unit="tsp.", ingredient_name="vanilla"),
    )
    instructions: tuple[str, ...] = (
        "Do not forget to sift dry ingredients.",
        "Combine until smooth in stand mixer.",
        "Spread on doughtnuts immediately.",
    )


default_recipe_registry.add_recipe(recipe=ChocolateDoughnutIcing())
