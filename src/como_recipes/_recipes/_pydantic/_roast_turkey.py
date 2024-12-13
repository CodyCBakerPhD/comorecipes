from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class RoastTurkey(Recipe):
    name: str = "Roast Turkey"
    tags: tuple[str, ...] = ("American", "Entree")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="large", ingredient_name="turkey bag"),
        IngredientRegistry.get_measurement(amount=8, unit="quarts", ingredient_name="water"),
        IngredientRegistry.get_measurement(amount=2, unit="cups", ingredient_name="Kosher salt"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="brown sugar"),
        IngredientRegistry.get_measurement(amount=20, unit="lb.", ingredient_name="whole turkey"),
    )
    instructions: tuple[str, ...] = (
        "Two days before roasting, bring water and salt to boil in large pot.",
        "When clear, remove from heat and add sugar.",
        "Refridgerate overnight.",
        "Rinse turkey and then place in a bag. Add the brine.",
        "Refridgerate together for 8-12 hours overnight.",
        "Wash turkey. Spatchcock.",
        "Roast for 4.25 - 4.75 hours at 325 F.",
        "Bird is fully cooked when thickest part is 180 F.",
        "Remove foil for last 30 minutes to allow crisping.",
    )


default_recipe_registry.add_recipe(recipe=RoastTurkey())
