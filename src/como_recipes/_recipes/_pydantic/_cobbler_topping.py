from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class CobblerTopping(Recipe):
    name: str = "Cobbler Topping"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 3, unit="cup", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=1 / 6, unit="cup", ingredient_name="white sugar"),
        IngredientRegistry.get_measurement(amount=1 / 6, unit="cup", ingredient_name="brown sugar"),
        IngredientRegistry.get_measurement(amount=1, unit="large", ingredient_name="egg"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="vanilla"),
        IngredientRegistry.get_measurement(amount=30, unit="grams", ingredient_name="flour"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="tsp.", ingredient_name="baking powder"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="tsp.", ingredient_name="salt"),
    )
    instructions: tuple[str, ...] = (
        "Cream butter and sugar until light and fluffy.",
        "Mix flour, baking powder, and salt in separate bowl.",
        "Slowly incorporate flour mixture into butter mixture, until just combined.",
        "Drop spoonfuls onto wet mixture.",
        "Bake for 40 min at 375 F.",
    )


default_recipe_registry.add_recipe(recipe=CobblerTopping())
