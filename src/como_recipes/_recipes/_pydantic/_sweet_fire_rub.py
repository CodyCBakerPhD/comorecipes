from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class SweetFireRub(Recipe):
    name: str = "Sweet Fire Rub"
    tags: tuple[str, ...] = ("American", "Vegetarian", "Spicy")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="brown sugar"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="white sugar"),
        IngredientRegistry.get_measurement(amount=38, unit="grams", ingredient_name="paprika"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp", ingredient_name="onion powder"),
        IngredientRegistry.get_measurement(amount=10, unit="grams", ingredient_name="garlic powder"),
        IngredientRegistry.get_measurement(amount=8, unit="grams", ingredient_name="chili powder"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp", ingredient_name="cayenne pepper"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp", ingredient_name="salt & pepper"),
    )
    instructions: tuple[str, ...] = ("Mix together and store in pantry.",)


default_recipe_registry.add_recipe(recipe=SweetFireRub())
