from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class FettuccineAlfredo(Recipe):
    name: str = "Fettuccine Alfredo"
    tags: tuple[str, ...] = ("Italian",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=3, unit="eggs", name="worth of fettuccine noodles"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", name="butter"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", name="heavy cream"),
        IngredientRegistry.get_measurement(amount=3, unit="cloves", name="crushed garlic"),
        IngredientRegistry.get_measurement(amount=1, unit="1/2", name="cups freshly grated Parmesan"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tbsp.", name="fresh parsley"),
    )
    instructions: tuple[str, ...] = (
        "Melt butter in saucepan over medium heat.",
        "Add cream and garlic, simmer for 5 minutes.",
        "Add most of the cheese, whisk quickly.",
        "Add rest of cheese just before serving.",
        "Garnish with the parsley if desired.",
    )


default_recipe_registry.add_recipe(recipe=FettuccineAlfredo())
