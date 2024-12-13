from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class ItalianMeringue(Recipe):
    name: str = "Italian Meringue"
    tags: tuple[str, ...] = ("Italian", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="cup", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="water"),
        IngredientRegistry.get_measurement(amount=4, unit="egg", ingredient_name="whites, room temperature"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", ingredient_name="cream of tartar or lemon juice"),
    )
    instructions: tuple[str, ...] = (
        "Combine sugar and water in a small saucepan over high heat, brushing down sides of pot as necessary with a pastry brush dipped in water.",
        "Cook until syrup is 270 F.",
        "Combine egg whites and cream of tartar (or lemon juice) in a stand mixer with a whisk attachment.",
        "Whisk at medium speed until soft peaks form (about 2 minutes).",
        "With the mixture running, slowly drizzle in the hot syrup.",
        "Increase mixer speed to high and whisk until stiff peaks are formed.",
    )


default_recipe_registry.add_recipe(recipe=ItalianMeringue())
