from ._base._base_measurement import Measurement
from ._base._sufficient_measurement import SufficientMeasurement
from ._base._base_recipe import Recipe
from ._base._base_ingredient import Ingredient
from ._base._base_meal import Meal
from ._registration._ingredient_registry import IngredientRegistry, default_ingredient_registry
from ._registration._recipe_registry import RecipeRegistry
from ._registration._default_recipe_registry import default_recipe_registry
from ._base._meal_selection import MealSelection

__all__ = [
    # Global variables
    "default_recipe_registry",
    "default_ingredient_registry",
    # Public API classes
    "Ingredient",
    "Recipe",
    "Meal",
    "Measurement",
    "SufficientMeasurement",
    "RecipeRegistry",
    "IngredientRegistry",
    "MealSelection",
    # Public submodules
    "app",
    "utils",
]

# Trigger import of hidden submodule elements (only need to import one item to trigger the rest)
# Used for automatic recipe registration as well as the isolated `app` submodule
from ._hidden_top_level_imports import _hide
