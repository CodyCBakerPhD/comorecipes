from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class SloppyJoe(Recipe):
    name: str = "Sloppy Joe"
    tags: tuple[str, ...] = ("American", "Vegetarian", "Entree")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="batch", ingredient_name="of Kaiser Rolls"),
        IngredientRegistry.get_measurement(amount=1, unit="lb", ingredient_name="ground beef or Boca crumbles"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="red onion"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", ingredient_name="garlic powder"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp.", ingredient_name="yellow mustard"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="ketchup"),
        IngredientRegistry.get_measurement(amount=3, unit="tsp.", ingredient_name="brown sugar"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tbsp.", ingredient_name="molasses"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="salt and pepper"),
    )
    instructions: tuple[str, ...] = ("Brown meat. Mix spices. Simmer until good consistency.",)


default_recipe_registry.add_recipe(recipe=SloppyJoe())
