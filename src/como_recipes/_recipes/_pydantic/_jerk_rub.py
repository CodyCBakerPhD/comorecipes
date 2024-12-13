from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class JerkRub(Recipe):
    name: str = "Jerk Rub"
    tags: tuple[str, ...] = ("Jamaican", "Vegetarian", "Entree")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", ingredient_name="garlic powder"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", ingredient_name="cumin"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="coriander"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="paprika"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="salt and pepper"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="olive oil"),
    )
    instructions: tuple[str, ...] = (
        "Mix dry ingredients and use oil to bind. For cooking with chicken, lather all sides and grill for 4-6 minutes on each side.",
    )


default_recipe_registry.add_recipe(recipe=JerkRub())
