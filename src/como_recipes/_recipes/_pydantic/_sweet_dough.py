from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class SweetDough(Recipe):
    name: str = "Sweet Dough"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=2 / 3, unit="cup", ingredient_name="whole milk"),
        IngredientRegistry.get_measurement(amount=5, unit="tbsp.", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=7 / 4, unit="tsp.", ingredient_name="yeast"),
        IngredientRegistry.get_measurement(amount=2, unit="eggs,", ingredient_name="room temperature"),
        IngredientRegistry.get_measurement(amount=11 / 4, unit="cups", ingredient_name="flour"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="butter, room temperature"),
    )
    instructions: tuple[str, ...] = (
        "Heat milk to 110 F in small saucepan over medium heat.",
        "Stir in 1 tbsp. sugar and yeast.",
        "Let sit for 5 minutes.",
        "Add eggs.",
        "Combine remaining dry ingredients then knead into dough.",
        "Let prove for 90 minutes.",
    )


default_recipe_registry.add_recipe(recipe=SweetDough())
