from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class BroccoliCheddarSoup(Recipe):
    name: str = "Broccoli Cheddar Soup"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", name="butter"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="large", name="onion"),
        IngredientRegistry.get_measurement(amount=8, unit="oz.", name="broccoli"),
        IngredientRegistry.get_measurement(amount=7, unit="oz.", name="not-chicken broth"),
        IngredientRegistry.get_measurement(amount=8, unit="oz.", name="cheddar"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", name="milk"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tbsp.", name="garlic powder"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="cup", name="cornstarch"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", name="water"),
    )
    instructions: tuple[str, ...] = (
        "In pot, melt butter over medium heat. Cook onion until softened. Stir in broccoli and cover with not-chicken broth. Simmer until tender, 10-15 minutes.",
        "Reduce heat and stir in cheese cubes until melted. Mix in milk and garlic powder. In a small bowl, stir cornstarch into water until dissolved.",
        "Stir mixture into soup, cook, stirring frequently, until thick.",
    )


default_recipe_registry.add_recipe(recipe=BroccoliCheddarSoup())
