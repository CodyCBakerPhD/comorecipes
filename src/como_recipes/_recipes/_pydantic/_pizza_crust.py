from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class PizzaCrust(Recipe):
    name: str = "Pizza Crust"
    tags: tuple[str, ...] = ("American", "Vegetarian", "Entree")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="cup", ingredient_name="water"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp", ingredient_name="yeast"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp", ingredient_name="sugar or honey"),
        IngredientRegistry.get_measurement(amount=255, unit="grams", ingredient_name="flour"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp", ingredient_name="salt"),
    )
    instructions: tuple[str, ...] = (
        "Activate yeast. Mix in flour and salt until good consistency. Knead for 3 minutes. Place in oiled rising container. Set timer for 40 minutes and let rise in warm spot.",
        "Preheat oven to 400 F. Press into shape and top. Brush sides with truffle oil and seasoning. Bake for around 13 minutes.",
    )


default_recipe_registry.add_recipe(recipe=PizzaCrust())
