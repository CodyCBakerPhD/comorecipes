from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class CabbageRolls(Recipe):
    name: str = "Cabbage Rolls"
    tags: tuple[str, ...] = ("Asian", "Vegetarian", "Entree")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=5 / 4, unit="cups", ingredient_name="white rice"),
        IngredientRegistry.get_measurement(amount=1, unit="large", ingredient_name="napa cabbage"),
        IngredientRegistry.get_measurement(amount=250, unit="grams", ingredient_name="white onion"),
        IngredientRegistry.get_measurement(amount=3 / 4, unit="tbsp", ingredient_name="ginger, minced"),
        IngredientRegistry.get_measurement(amount=15, unit="grams", ingredient_name="garlic"),
        IngredientRegistry.get_measurement(amount=1, unit="minced", ingredient_name="carrot"),
        IngredientRegistry.get_measurement(amount=2, unit="minced", ingredient_name="peppers"),
        IngredientRegistry.get_measurement(amount=8, unit="minced", ingredient_name="shittake mushrooms"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp", ingredient_name="tamari"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", ingredient_name="pepper"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", ingredient_name="onion powder"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp", ingredient_name="red pepper flakes"),
    )
    instructions: tuple[str, ...] = (
        "Soak rice in bowl 60 minutes before cooking. Cook in 5/3 cup water and 1 tbsp butter; reach boiling before reducing to simmer until all water is gone.",
        "Prep cabbage leaves by chopping off thickest bottom portion then boiling a large pot of water and adding 3-4 leaves at a time for 1 minute until softened. When done, place them into bowl of cold water and set aside.",
        "Heat some peanut oil in a skillet and saute vegetables for 4 minutes; then add tamari and remaining spices. Cook for another 2 minutes.",
        "Combine rice and vegetable mixture. Season to taste.",
        "To assemble, add about 1 tbsp of mixture to a single cabbage leaf, fold and roll together.",
        "Pan sear the rolls in large skillet for a few minutes on all sides; rolls should be golden brown.",
        "Garnish with sesame seeds. Recommend topping with Tamari Sauce for extra flavor.",
    )


default_recipe_registry.add_recipe(recipe=CabbageRolls())
