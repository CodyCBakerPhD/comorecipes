from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class EnchiladaSauce(Recipe):
    name: str = "Enchilada Sauce"
    tags: tuple[str, ...] = ("Mexican", "Vegetarian", "Entree", "Spicy")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="vegetable oil"),
        IngredientRegistry.get_measurement(amount=15, unit="grams", ingredient_name="flour"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="dark chili powder"),
        IngredientRegistry.get_measurement(amount=8, unit="oz.", ingredient_name="can tomato sauce"),
        IngredientRegistry.get_measurement(amount=3 / 2, unit="cups", ingredient_name="water"),
        IngredientRegistry.get_measurement(amount=1, unit="grams", ingredient_name="cumin"),
        IngredientRegistry.get_measurement(amount=1, unit="grams", ingredient_name="garlic powder"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp", ingredient_name="onion powder"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="tsp", ingredient_name="salt"),
    )
    instructions: tuple[str, ...] = (
        "Heat oil over medium-high heat. Stir in flour and chili powder.",
        "Reduce heat to medium and cook till lightly brown stirring constantly.",
        "Reduce heat to medium-low and gradually incorporate other spices.",
        "Cook about 10-20 minutes until desired consistency.",
        "Makes enough sauce for 2 personal pans (two tortillas each) or 1 large pans (about 4-6 tortillas each).",
        "DO NOT USE COTIJA CHEESE IN THE ENCHILADAS.",
    )


default_recipe_registry.add_recipe(recipe=EnchiladaSauce())
