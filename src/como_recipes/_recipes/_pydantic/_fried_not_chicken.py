from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class FriedNotChicken(Recipe):
    name: str = "Fried Not Chicken"
    tags: tuple[str, ...] = ("American", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 4, unit="serving", ingredient_name="of Frying Breading"),
        IngredientRegistry.get_measurement(amount=4, unit="individual", ingredient_name="not-chicken tenders"),
        IngredientRegistry.get_measurement(amount=2, unit="cups", ingredient_name="buttermilk"),
    )
    instructions: tuple[str, ...] = (
        "Heat oil to 325 F. Add some lime juice if feeling fruity.",
        "Soak tenders in buttermilk for a few minutes.",
        "Dredge with breading in a plastic bag for maximum cleanliness and adherence.",
        "Fry for ~13 minutes until golden brown and crispy.",
    )


default_recipe_registry.add_recipe(recipe=FriedNotChicken())
