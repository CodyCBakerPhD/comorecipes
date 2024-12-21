from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class OldFashionedChocolateFudge(Recipe):
    name: str = "Old Fashioned Chocolate Fudge"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian", "Chocolate")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=600, unit="grams", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=57, unit="grams", ingredient_name="dutch cocoa"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=366, unit="grams", ingredient_name="whole milk"),
        IngredientRegistry.get_measurement(amount=57, unit="grams", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp", ingredient_name="vanilla"),
    )
    instructions: tuple[str, ...] = (
        "Butter heat-proof pan.",
        "Combine sugar, cocoa, and salt..",
        "Combine with milk.",
        "While stirring constantly, heat over medium heat until strong boil, approximately 15 minutes.",
        "Lower heat to medium-low and cook approximately 30 more minutes.",
        "Target temperature is 234 F.",
        "Remove from heat and add butter and vanilla.Carefully transfer to a stand mixer bowl.",
        "Contents will be very hot, so be careful.",
        "Carefully beat with scraper attachment (and shield) on lowest speed until no longer shiny, about 6 minutes.",
        "Pour fudge onto prepared pan and let cool.",
    )
    notes: tuple[str, ...] = ("Constantly stir to avoid any amount of burning.",)


default_recipe_registry.add_recipe(recipe=OldFashionedChocolateFudge())
