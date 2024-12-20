from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class AglioEOlio(Recipe):
    name: str = "Aglio E Olio"
    tags: tuple[str, ...] = ("Italian", "Pasta", "Vegetarian", "Entree")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=2, unit="qt.", ingredient_name="water"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1, unit="lb.", ingredient_name="thin spaghetti"),
        IngredientRegistry.get_measurement(amount=1 / 3, unit="cup", ingredient_name="olive oil"),
        IngredientRegistry.get_measurement(amount=8, unit="large", ingredient_name="cloves of garlic"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp", ingredient_name="crushed red pepper"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="parsley"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", ingredient_name="fresh Parmesan"),
    )
    instructions: tuple[str, ...] = (
        "Bring water and salt to boil. Cook pasta. Set aside 3/2 cup of pasta water before draining.",
        "Heat olive oil over medium heat in a large pot.",
        "Add garlic and cook for 1-2 minutes, stirring frequently until it just turns golden.",
        "Add red pepper and cook 30 seconds more.",
        "Carefully add reserved pasta water and bring to boil.",
        "Lower heat and simmer for 5 minutes, until liquid is reduced by about a third.",
        "Incorporate pasta, parsley, and Permesan.",
    )


default_recipe_registry.add_recipe(recipe=AglioEOlio())
