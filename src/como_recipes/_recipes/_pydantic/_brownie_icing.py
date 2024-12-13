from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class BrownieIcing(Recipe):
    name: str = "Brownie Icing"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian", "chocolate")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="sifted Dutch cocoa"),
        IngredientRegistry.get_measurement(amount=3 / 2, unit="tbsp.", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cups", ingredient_name="sifted powdered sugar"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="evaporated milk"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", ingredient_name="vanilla"),
    )
    instructions: tuple[str, ...] = (
        "Do not forget to sift dry ingredients.",
        "Melt butter in saucepan. Add sifted cocoa and remove pan from heat.",
        "Stir in sifted powdered sugar and other ingredients, saving vanilla for last to keep it smooth.",
        "Add more powdered sugar as necessary for consistency.",
    )


default_recipe_registry.add_recipe(recipe=BrownieIcing())
