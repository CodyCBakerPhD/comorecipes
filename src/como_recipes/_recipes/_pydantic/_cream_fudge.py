from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class CreamFudge(Recipe):
    name: str = "Cream Fudge"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian", "Christmas")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=400, unit="grams", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=187, unit="grams", ingredient_name="whole milk"),
        IngredientRegistry.get_measurement(amount=22, unit="grams", ingredient_name="light corn syrup"),
        IngredientRegistry.get_measurement(amount=170, unit="grams", ingredient_name="condensed milk"),
        IngredientRegistry.get_measurement(amount=76, unit="grams", ingredient_name="unsalted butter"),
    )
    instructions: tuple[str, ...] = (
        'Grease 13" x 9" baking pan.',
        "Combine sugar and whole milk into large saucepan.",
        "Add condensed milk, corn syrup, and butter.",
        "Heat over medium-high heat for approximately 20-30 minutes, stirring constantly.",
        "Target temperature is 240 F, which should be thick and caramelized.",
        "Remove from heat and transfer to a stand mixer bowl.",
        "Contents will be very hot, so be careful.",
        "Beat with scraper attachment on lowest speed until fudge is no longer shiny, approximately 5-7 minutes.",
        "Pour fudge onto prepared pan and let cool.",
    )


default_recipe_registry.add_recipe(recipe=CreamFudge())
