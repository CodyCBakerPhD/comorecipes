from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class BlackBeanChili(Recipe):
    name: str = "Black Bean Chili"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=4, unit="cloves", name="garlic"),
        IngredientRegistry.get_measurement(amount=1 / 3, unit="white", name="onion, minced"),
        IngredientRegistry.get_measurement(amount=1, unit="qt", name="jar of canned garden tomatoes"),
        IngredientRegistry.get_measurement(amount=4, unit="tbsp", name="chili powder"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp", name="cumin"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp", name="oregano"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp", name="salt"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", name="cayenne pepper"),
        IngredientRegistry.get_measurement(amount=1, unit="can", name="black beans"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp", name="peanut oil"),
    )
    instructions: tuple[str, ...] = (
        "Carefully caramelize onions and garlic. Add tomatoes. Mix all dry ingredients separately and add to mixture. Add beans and oil. Stir and simmer for at least 15 minutes.",
    )


default_recipe_registry.add_recipe(recipe=BlackBeanChili())
