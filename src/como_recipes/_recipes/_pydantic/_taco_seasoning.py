from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class TacoSeasoning(Recipe):
    name: str = "Taco Seasoning"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 4, unit="", name="tsp. garlic powder"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="", name="tsp. onion powder"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="", name="tsp. red pepper"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="", name="tsp. dried oregano"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="", name="tsp. paprika"),
        IngredientRegistry.get_measurement(amount=3 / 2, unit="tsp.", name="cumin"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="", name="tsp. salt"),
        IngredientRegistry.get_measurement(amount=1, unit="", name="tsp. pepper"),
        IngredientRegistry.get_measurement(amount=1, unit="", name="lb. ground beef or refried beans or Boca"),
    )
    instructions: tuple[str, ...] = (
        "Mix spice.",
        "To use spice to make tacos, brown beef or boca.",
        "Add mix and some water for incorporation (beef or Boca).",
        "Cook off excess water to allow base to absorb spice.",
    )


default_recipe_registry.add_recipe(recipe=TacoSeasoning())
