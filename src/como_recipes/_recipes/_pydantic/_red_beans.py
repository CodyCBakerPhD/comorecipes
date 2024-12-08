from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class RedBeans(Recipe):
    name: str = "Red Beans"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="recipes", name="worth of rice"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", name="olive oil"),
        IngredientRegistry.get_measurement(amount=4, unit="cloves", name="garlic"),
        IngredientRegistry.get_measurement(amount=1 / 3, unit="white", name="onion"),
        IngredientRegistry.get_measurement(amount=1, unit="stalk", name="celery"),
        IngredientRegistry.get_measurement(amount=2, unit="bay", name="leaves"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="cayenne pepper"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", name="thyme"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="tsp.", name="sage"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", name="parsley"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", name="Cajun seasoning"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", name="water"),
    )
    instructions: tuple[str, ...] = (
        "Make rice. Mix spices together.",
        "Carefully caramelize garlic, onion, and celery in oil.",
        "Add water to onions and garlic, then mix in spices.",
        "Add beans and any other add-ins, simmer for at least 15 minutes.",
        "Serve on rice.",
    )


default_recipe_registry.add_recipe(recipe=RedBeans())
