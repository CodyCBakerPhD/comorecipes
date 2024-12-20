from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class Applesauce(Recipe):
    name: str = "Applesauce"
    tags: tuple[str, ...] = ("American", "Dessert", "Side", "Vegetarian", "Fruit")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=4, unit="large", ingredient_name="apples"),
        IngredientRegistry.get_measurement(amount=3 / 4, unit="cup", ingredient_name="water"),
        IngredientRegistry.get_measurement(amount=1 / 16, unit="cup", ingredient_name="white sugar"),
        IngredientRegistry.get_measurement(amount=1 / 16, unit="cup", ingredient_name="brown sugar"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", ingredient_name="ground cinnamon"),
    )
    instructions: tuple[str, ...] = (
        "Peel and core apples.",
        "Combine everything and cook over medium heat for 15-20 minutes (until apples are soft).",
        "Allow to cool, then mash with fork or potato masher.",
    )


default_recipe_registry.add_recipe(recipe=Applesauce())
