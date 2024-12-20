from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class BroccoliCheddarSoup(Recipe):
    name: str = "Broccoli Cheddar Soup"
    tags: tuple[str, ...] = ("American", "Vegetarian", "Entree", "Soup")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="large", ingredient_name="onion"),
        IngredientRegistry.get_measurement(amount=8, unit="oz.", ingredient_name="broccoli"),
        IngredientRegistry.get_measurement(amount=7, unit="oz.", ingredient_name="not-chicken broth"),
        IngredientRegistry.get_measurement(amount=8, unit="oz.", ingredient_name="cheddar"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", ingredient_name="milk"),
        IngredientRegistry.get_measurement(amount=5, unit="grams", ingredient_name="garlic powder"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="cup", ingredient_name="cornstarch"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="water"),
    )
    instructions: tuple[str, ...] = (
        "In pot, melt butter over medium heat. Cook onion until softened. Stir in broccoli and cover with not-chicken broth. Simmer until tender, 10-15 minutes.",
        "Reduce heat and stir in cheese cubes until melted. Mix in milk and garlic powder. In a small bowl, stir cornstarch into water until dissolved.",
        "Stir mixture into soup, cook, stirring frequently, until thick.",
    )


default_recipe_registry.add_recipe(recipe=BroccoliCheddarSoup())
