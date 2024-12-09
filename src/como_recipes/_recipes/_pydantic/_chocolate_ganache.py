from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class ChocolateGanache(Recipe):
    name: str = "Chocolate Ganache"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=2, unit="cups", ingredient_name="semi-sweet chocolate"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="heavy cream"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", ingredient_name="vanilla extract"),
    )
    instructions: tuple[str, ...] = (
        "Combine chocolate and heavy cream in a small saucepan over medium heat.",
        "Stir frequently until chocolate is melted and mixture is smooth.",
        "Remove from heat, stir in vanilla extract.",
        "Allow chocolate to cool slightly, about 5 minutes.",
    )


default_recipe_registry.add_recipe(recipe=ChocolateGanache())
