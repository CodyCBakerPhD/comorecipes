from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class PumpkinPieFilling(Recipe):
    name: str = "Pumpkin Pie Filling"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=15, unit="oz.", ingredient_name="fresh pumpkin puree"),
        IngredientRegistry.get_measurement(amount=14, unit="oz.", ingredient_name="condensed milk"),
        IngredientRegistry.get_measurement(amount=2, unit="eggs", ingredient_name=""),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", ingredient_name="ginger"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", ingredient_name="nutmeg"),
        IngredientRegistry.get_measurement(amount=3, unit="grams", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="pie", ingredient_name="crust"),
    )
    instructions: tuple[str, ...] = ("Mix ingredients well and pour into pie crust. Bake for 15 minutes at 425 F.",)


default_recipe_registry.add_recipe(recipe=PumpkinPieFilling())
