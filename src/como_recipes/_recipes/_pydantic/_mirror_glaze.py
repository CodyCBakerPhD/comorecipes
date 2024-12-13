from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class MirrorGlaze(Recipe):
    name: str = "Mirror Glaze"
    tags: tuple[str, ...] = ("Vegetarian", "Dessert", "Vegetarian", "Chocolate")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=20, unit="g", ingredient_name="Agar Agar"),
        IngredientRegistry.get_measurement(amount=170, unit="mL", ingredient_name="water"),
        IngredientRegistry.get_measurement(amount=300, unit="mL", ingredient_name="corn syrup"),
        IngredientRegistry.get_measurement(amount=150, unit="g", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=200, unit="g", ingredient_name="condensed milk"),
        IngredientRegistry.get_measurement(amount=300, unit="g", ingredient_name="white chocolate"),
    )
    instructions: tuple[str, ...] = (
        "Divide water in two.",
        "Place Agar Agar in one of the two halves and let sit for 4 minutes.",
        "In a large saucepan - add corn syrup, condensed milk, and remaining water over low to medium heat.",
        "Bring to slow boil, ensuring sugar has dissolved.",
        "Take saucepan off heat, let rest 1 minute before adding white chocolate to mixture.",
        "Add Agar Agar and let mixture melt.",
        "Stir and allow glaze to come to room temperature.",
    )


default_recipe_registry.add_recipe(recipe=MirrorGlaze())
