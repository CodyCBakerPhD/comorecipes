from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class CollardGreens(Recipe):
    name: str = "Collard Greens"
    tags: tuple[str, ...] = ("American", "Side", "Vegetarian", "Spicy")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=3, unit="tbsp", ingredient_name="olive oil"),
        IngredientRegistry.get_measurement(amount=250, unit="grams", ingredient_name="white onion"),
        IngredientRegistry.get_measurement(amount=10, unit="grams", ingredient_name="garlic"),
        IngredientRegistry.get_measurement(amount=6, unit="grams", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp", ingredient_name="pepper"),
        IngredientRegistry.get_measurement(amount=3, unit="cups", ingredient_name="chicken flavored vegetable broth"),
        IngredientRegistry.get_measurement(amount=1, unit="pinch", ingredient_name="red pepper flakes"),
        IngredientRegistry.get_measurement(amount=1, unit="lb.", ingredient_name="fresh collard greens"),
    )
    instructions: tuple[str, ...] = (
        "Heat oil in very large pot over medium heat.",
        "Add onion, cook until tender. Add garlic. Add collard greens, fry until they wilt.",
        "Pour in broth, season with spices. Reduce heat to low, cover, and simmer for 45 minutes or until tender.",
    )


default_recipe_registry.add_recipe(recipe=CollardGreens())
