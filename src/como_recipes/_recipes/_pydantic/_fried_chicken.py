from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class FriedChicken(Recipe):
    name: str = "Fried Chicken"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 4, unit="serving", ingredient_name="of Frying Breading"),
        IngredientRegistry.get_measurement(amount=2, unit="large", ingredient_name="chicken breasts"),
        IngredientRegistry.get_measurement(amount=2, unit="cups", ingredient_name="buttermilk"),
    )
    instructions: tuple[str, ...] = (
        "Heat oil to 325 F. Add some lime juice if feeling fruity.",
        "Cut each chicken breast in half and soak in buttermilk for a few minutes.",
        "Dredge with breading in a plastic bag for maximum cleanliness and adherence.",
        "Fry for ~13 minutes until golden brown, crispy, and thickest part of meat is 180 F.",
    )


default_recipe_registry.add_recipe(recipe=FriedChicken())
