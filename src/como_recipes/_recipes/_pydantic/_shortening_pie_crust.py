from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class ShorteningPieCrust(Recipe):
    name: str = "Shortening Pie Crust"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=2, unit="tsp", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=270, unit="grams", ingredient_name="flour"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", ingredient_name="cold shortening"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="ice water"),
        IngredientRegistry.get_measurement(amount=1, unit="egg", ingredient_name="yolk with a little water"),
    )
    instructions: tuple[str, ...] = (
        "Pulse flour, sugar and salt in food processor to combine. Add cold shortening and pulse until pea-size pieces remain.",
        "Transfer to bowl and cover, refrigerate for at least 30 minutes. Drizzle ice water over mixture and mix thoroughly with hands.",
        "Divide in half, press into discs and store back in the refrigerator for at least 1 hour.",
        "Preheat to 350 F. Move discs into pie tin. Shape and add filling, then top. Seal joint and add air-holes in the top. Brush top with egg yolk and water mixture, not overdoing it.",
        "Bake for 90 to 100 minutes for fruit pies.",
    )


default_recipe_registry.add_recipe(recipe=ShorteningPieCrust())
