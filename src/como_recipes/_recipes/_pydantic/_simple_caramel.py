from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class SimpleCaramel(Recipe):
    name: str = "Simple Caramel"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=14, unit="oz.", ingredient_name="sweetened condensed milk"),
        IngredientRegistry.get_measurement(amount=7, unit="tbsp", ingredient_name="butter, cut into pieces"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="brown sugar"),
        IngredientRegistry.get_measurement(amount=1 / 6, unit="cup", ingredient_name="light corn syrup"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", ingredient_name="vanilla extract"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="tsp", ingredient_name="salt"),
    )
    instructions: tuple[str, ...] = (
        "Combine condensed milk, butter, brown sugar, and corn syrup in medium saucepan over medium heat.",
        "Stir frequently until butter is melted and ingredients are combined.",
        "Continue to constantly stir until mixture begins to boil.",
        "Once mixture begins to boil, reduce heat to simmer and continue to stir.",
        "Continue for 8-10 minutes until mixture has thickened and darkened.",
        "Remove from heat and immediately mix in vanilla extract and salt.",
    )


default_recipe_registry.add_recipe(recipe=SimpleCaramel())
