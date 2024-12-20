from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class RedWineSauce(Recipe):
    name: str = "Red Wine Sauce"
    tags: tuple[str, ...] = ("Italian", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="tbsp", ingredient_name="olive oil"),
        IngredientRegistry.get_measurement(amount=10, unit="grams", ingredient_name="garlic"),
        IngredientRegistry.get_measurement(amount=3 / 4, unit="cup", ingredient_name="red wine"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="water"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp", ingredient_name="soy sauce"),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp", ingredient_name="parsley"),
    )
    instructions: tuple[str, ...] = (
        "Heat oil over medium-high heat. Cook garlic for ~30 seconds. Add wine and reach a simmer.",
        "Reduce to half, about 2-3 minutes. Add water and soy sauce. Reduce to half again.",
        "Reduce heat to medium-low and whisk in butter, 1 tbsp at a time. Stir in parsley and serve.",
    )


default_recipe_registry.add_recipe(recipe=RedWineSauce())
