from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class TacoSeasoning(Recipe):
    name: str = "Taco Seasoning"
    tags: tuple[str, ...] = ("American", "Vegetarian", "Entree", "Spicy")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 4, unit="", ingredient_name="tsp garlic powder"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="", ingredient_name="tsp onion powder"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="", ingredient_name="tsp red pepper"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="", ingredient_name="tsp dried oregano"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="", ingredient_name="tsp paprika"),
        IngredientRegistry.get_measurement(amount=8, unit="grams", ingredient_name="cumin"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="", ingredient_name="tsp salt"),
        IngredientRegistry.get_measurement(amount=1, unit="", ingredient_name="tsp pepper"),
        IngredientRegistry.get_measurement(
            amount=1,
            unit="",
            ingredient_name="lb. ground beef or refried beans or Boca",
        ),
    )
    instructions: tuple[str, ...] = (
        "Mix spice.",
        "To use spice to make tacos, brown beef or boca.",
        "Add mix and some water for incorporation (beef or Boca).",
        "Cook off excess water to allow base to absorb spice.",
    )


default_recipe_registry.add_recipe(recipe=TacoSeasoning())
