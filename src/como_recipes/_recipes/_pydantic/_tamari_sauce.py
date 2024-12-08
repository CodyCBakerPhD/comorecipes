from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class TamariSauce(Recipe):
    name: str = "Tamari Sauce"
    tags: tuple[str, ...] = ("Asian",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", name="sesame oil"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tbsp.", name="ginger, minced"),
        IngredientRegistry.get_measurement(amount=2, unit="cloves", name="garlic, minced"),
        IngredientRegistry.get_measurement(amount=3 / 2, unit="tbsp.", name="tamari"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", name="rice vinegar"),
        IngredientRegistry.get_measurement(amount=3 / 4, unit="tbsp.", name="maple syrup"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", name="water"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tbsp.", name="cornstarch"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="salt"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="pepper"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="red pepper flakes"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="paprika"),
    )
    instructions: tuple[str, ...] = (
        "Mix water and cornstarch to make a slurry.",
        "Heat oil in saucepan. Add everything except cornstarch mixture, cook for 2 minutes.",
        "Add cornstarch mixture to thicken.",
        "Season with spices, cook until desired consistency.",
    )


default_recipe_registry.add_recipe(recipe=TamariSauce())
