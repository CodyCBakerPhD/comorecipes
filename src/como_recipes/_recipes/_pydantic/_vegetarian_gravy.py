from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class VegetarianGravy(Recipe):
    name: str = "Vegetarian Gravy"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", name="butter"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", name="flour"),
        IngredientRegistry.get_measurement(amount=2, unit="cups", name="not-chicken stock"),
        IngredientRegistry.get_measurement(amount=1 / 3, unit="cup", name="heavy cream"),
        IngredientRegistry.get_measurement(amount=5 / 4, unit="tsp.", name="salt and pepper"),
        IngredientRegistry.get_measurement(amount=1 / 6, unit="tsp.", name="paprika"),
    )
    instructions: tuple[str, ...] = ("Make roux with butter and flour. Thicken with stock. Season.",)


default_recipe_registry.add_recipe(recipe=VegetarianGravy())
