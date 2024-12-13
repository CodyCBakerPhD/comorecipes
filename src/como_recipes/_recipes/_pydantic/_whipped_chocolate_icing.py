from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class WhippedChocolateIcing(Recipe):
    name: str = "Whipped Chocolate Icing"
    tags: tuple[str, ...] = ("American", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=11 / 4, unit="cups", ingredient_name="sifted powdered sugar"),
        IngredientRegistry.get_measurement(amount=6, unit="tbsp.", ingredient_name="cocoa powder"),
        IngredientRegistry.get_measurement(amount=6, unit="tbsp.", ingredient_name="room-temperature butter"),
        IngredientRegistry.get_measurement(amount=5, unit="tbsp.", ingredient_name="evaporated milk"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="vanilla extract"),
    )
    instructions: tuple[str, ...] = (
        "Sift the cocoa powder and powdered sugar together.",
        "In a separate bowl, cream butter until smooth and gradually beat in sugar and evaporated milk.",
        "Blend in vanilla.",
        "Beat until light and fluffy.",
    )


default_recipe_registry.add_recipe(recipe=WhippedChocolateIcing())
