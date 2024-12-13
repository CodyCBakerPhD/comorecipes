from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class KaleSoup(Recipe):
    name: str = "Kale Soup"
    tags: tuple[str, ...] = ("American", "Vegetarian", "Entree", "Soup")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", ingredient_name="olive oil"),
        IngredientRegistry.get_measurement(amount=1, unit="yellow", ingredient_name="onion, chopped"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", ingredient_name="garlic, chopped"),
        IngredientRegistry.get_measurement(
            amount=1,
            unit="bunch",
            ingredient_name="of kale, stems removed and leaves chopped",
        ),
        IngredientRegistry.get_measurement(amount=8, unit="cups", ingredient_name="water"),
        IngredientRegistry.get_measurement(amount=6, unit="cubes", ingredient_name="of vegetable bouillon"),
        IngredientRegistry.get_measurement(amount=15, unit="oz.", ingredient_name="stewed tomatoes"),
        IngredientRegistry.get_measurement(amount=6, unit="white", ingredient_name="potatoes, cubed"),
        IngredientRegistry.get_measurement(
            amount=30,
            unit="oz",
            ingredient_name="cannellini beans (two 15 oz. cans), drained",
        ),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="Italian seasoning"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", ingredient_name="dried parsley"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="Salt and pepper"),
    )
    instructions: tuple[str, ...] = (
        "Heat olive oil in a large soup pot. Cook the onion and garlic until soft. Stir in the kale and cook until wilted (about 2 minutes).",
        "Stir in the water, bouillon, tomatoes, potatoes, beans, Italian seasoning, parsley.",
        "Simmer soup on medium heat for 25 minutes, or until potatoes are cooked through. Season with salt and pepper to taste.",
    )


default_recipe_registry.add_recipe(recipe=KaleSoup())
