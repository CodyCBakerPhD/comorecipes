from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class GreenBeanCasserole(Recipe):
    name: str = "Green Bean Casserole"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=2, unit="cans", ingredient_name="French-style green beans"),
        IngredientRegistry.get_measurement(amount=1, unit="can", ingredient_name="cream of mushroom soup"),
        IngredientRegistry.get_measurement(amount=1, unit="can", ingredient_name="French-fried onions"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="milk"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="tsp", ingredient_name="pepper"),
    )
    instructions: tuple[str, ...] = (
        "Drain green beans. Mix soup, milk, pepper in a bowl. Add beans and mix together. Add half of the onions, give a quick stir.",
        "Place in casserole dish and bake for 25 minutes at 350 F. Add remaining onions to top and bake another 5 minutes, keeping close watch for burning.",
    )


default_recipe_registry.add_recipe(recipe=GreenBeanCasserole())
