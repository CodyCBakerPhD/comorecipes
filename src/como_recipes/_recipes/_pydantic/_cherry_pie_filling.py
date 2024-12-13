from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class CherryPieFilling(Recipe):
    name: str = "Cherry Pie Filling"
    tags: tuple[str, ...] = ("American", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="pie", ingredient_name="crust"),
        IngredientRegistry.get_measurement(amount=4, unit="cups", ingredient_name="fresh tart cherries or"),
        IngredientRegistry.get_measurement(amount=6, unit="cups", ingredient_name="frozen tart cherries"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="cornstarch"),
    )
    instructions: tuple[str, ...] = (
        "Place cherries into a saucepan over medium heat and cover. Heat cherries until they release their juices and simmer 10 to 15 minutes. Stir often.",
        "In a bowl, whisk sugar with cornstarch until smooth. Pour mixture into cherries and juice and combine. Return to low heat, bring to simmer, and cook until filling has thickened (about 2 minutes).",
        "Remove from heat and use as pie filling. Cook to pie crust instructions.",
    )


default_recipe_registry.add_recipe(recipe=CherryPieFilling())
