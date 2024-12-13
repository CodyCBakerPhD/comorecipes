from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class RedBeans(Recipe):
    name: str = "Red Beans"
    tags: tuple[str, ...] = ("American", "Vegetarian", "Entree", "Spicy")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="recipes", ingredient_name="worth of rice"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="olive oil"),
        IngredientRegistry.get_measurement(amount=4, unit="cloves", ingredient_name="garlic"),
        IngredientRegistry.get_measurement(amount=1 / 3, unit="white", ingredient_name="onion"),
        IngredientRegistry.get_measurement(amount=1, unit="stalk", ingredient_name="celery"),
        IngredientRegistry.get_measurement(amount=2, unit="bay", ingredient_name="leaves"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", ingredient_name="cayenne pepper"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="thyme"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="tsp.", ingredient_name="sage"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="parsley"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="Cajun seasoning"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", ingredient_name="water"),
    )
    instructions: tuple[str, ...] = (
        "Make rice. Mix spices together.",
        "Carefully caramelize garlic, onion, and celery in oil.",
        "Add water to onions and garlic, then mix in spices.",
        "Add beans and any other add-ins, simmer for at least 15 minutes.",
        "Serve on rice.",
    )


default_recipe_registry.add_recipe(recipe=RedBeans())
