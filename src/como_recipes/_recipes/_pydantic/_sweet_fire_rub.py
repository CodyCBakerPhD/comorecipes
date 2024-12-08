from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class SweetFireRub(Recipe):
    name: str = "Sweet Fire Rub"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", name="brown sugar"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", name="white sugar"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", name="paprika"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", name="onion powder"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", name="garlic powder"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", name="chili powder"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", name="cayenne pepper"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", name="salt & pepper"),
    )
    instructions: tuple[str, ...] = ("Mix together and store in pantry.",)


default_recipe_registry.add_recipe(recipe=SweetFireRub())
