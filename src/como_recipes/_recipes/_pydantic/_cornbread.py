from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class Cornbread(Recipe):
    name: str = "Cornbread"
    tags: tuple[str, ...] = ("American", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=1 / 6, unit="cup", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=1, unit="large", ingredient_name="egg"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="buttermilk"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="baking soda"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="cornmeal"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="flour"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="salt"),
    )
    instructions: tuple[str, ...] = (
        "Preheat to 375 F. Melt butter. Stir in sugar. Add eggs, beat.",
        "Combine buttermilk and soda, stir into mixture.",
        "Add remaining ingredients, stir until blended.",
        "Bake for about 20 minutes, until slightly brown on top.",
    )


default_recipe_registry.add_recipe(recipe=Cornbread())
