from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class Brownies(Recipe):
    name: str = "Brownies"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="vegetable oil"),
        IngredientRegistry.get_measurement(amount=2 / 3, unit="cup", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=2, unit="large", ingredient_name="eggs"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="vanilla"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="baking powder"),
        IngredientRegistry.get_measurement(amount=1 / 3, unit="cup", ingredient_name="cocoa powder"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="flour"),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp.", ingredient_name="chocolate chips"),
    )
    instructions: tuple[str, ...] = (
        "Preheat to 350 F, spray pan.",
        "Mix oil and sugar well.",
        "Add eggs and vanilla, just barely blend in.",
        "Mix all dry ingredients separately, stir into oil mixture.",
        "Bake around 20 minutes.",
    )


default_recipe_registry.add_recipe(recipe=Brownies())
