from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class Carnitas(Recipe):
    name: str = "Carnitas"
    tags: tuple[str, ...] = ("Mexican",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="lb.", ingredient_name="pork shoulder"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="oregano"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp.", ingredient_name="cumin"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="chili powder"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="flour"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="salt and pepper"),
        IngredientRegistry.get_measurement(amount=2, unit="oranges,", ingredient_name="juiced"),
        IngredientRegistry.get_measurement(amount=2, unit="cloves", ingredient_name="minced garlic"),
    )
    instructions: tuple[str, ...] = (
        "Brown pork with dry spices rubbed in. Slow cook in other ingredients for 6-8 hours on low in a small slow-cooker.",
        "Remove and shred, reserving strained liquid. Crisp in large skillet with remaining juices until evaporated.",
    )


default_recipe_registry.add_recipe(recipe=Carnitas())
