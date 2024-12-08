from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class StirFry(Recipe):
    name: str = "Stir Fry"
    tags: tuple[str, ...] = ("Asian",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="rice"),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp", name="peanut oil"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="beef, chicken, pork, or shrimp"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="tofu"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="shallots"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="garlic"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="carrots"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="broccoli"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="cauliflower"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="cabbage"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="green beans"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="pea pods"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="spinach"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="water chestnut"),
    )
    instructions: tuple[str, ...] = (
        "Meat: cut into thin strips and fry in separate pan without onions/garlic",
        "Tofu: get extra-firm and deep fry covered in cornstarch",
        "In main woc, fry vegetables in order of cooking time (roughly given in order of ingredients). Add sauce and garnish with meat or tofu.",
    )


default_recipe_registry.add_recipe(recipe=StirFry())
