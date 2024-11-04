from ._base import Ingredient, MeasuredIngredient, Recipe
from ._registration import default_recipe_registry

__all__ = [
    "Ingredient",
    "MeasuredIngredient",
    "Recipe",
    "default_recipe_registry",  # Global variable
    "utils",  # Public submodule
]

# Trigger import of built-in recipes (only need to import one item to trigger the rest)
from ._recipes._pydantic import AglioEOlio
