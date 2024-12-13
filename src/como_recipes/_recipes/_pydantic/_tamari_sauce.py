from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class TamariSauce(Recipe):
    name: str = "Tamari Sauce"
    tags: tuple[str, ...] = ("Asian", "Side", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="sesame oil"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tbsp.", ingredient_name="ginger, minced"),
        IngredientRegistry.get_measurement(amount=2, unit="cloves", ingredient_name="garlic, minced"),
        IngredientRegistry.get_measurement(amount=3 / 2, unit="tbsp.", ingredient_name="tamari"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="rice vinegar"),
        IngredientRegistry.get_measurement(amount=3 / 4, unit="tbsp.", ingredient_name="maple syrup"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="water"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tbsp.", ingredient_name="cornstarch"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="pepper"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="red pepper flakes"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="paprika"),
    )
    instructions: tuple[str, ...] = (
        "Mix water and cornstarch to make a slurry.",
        "Heat oil in saucepan. Add everything except cornstarch mixture, cook for 2 minutes.",
        "Add cornstarch mixture to thicken.",
        "Season with spices, cook until desired consistency.",
    )


default_recipe_registry.add_recipe(recipe=TamariSauce())
