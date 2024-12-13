from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class KaiserRoll(Recipe):
    name: str = "Kaiser Roll"
    tags: tuple[str, ...] = ("American", "Side", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="cup", ingredient_name="water"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="yeast"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="sugar or honey"),
        IngredientRegistry.get_measurement(amount=1 / 6, unit="cup", ingredient_name="vegetable oil"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=2, unit="cups", ingredient_name="flour"),
    )
    instructions: tuple[str, ...] = (
        "Preheat oven to 400 F. Activate yeast.",
        "Mix in oil and flour and salt until good consistency. Roll out into shape (make sure the rolls are appropriately sized for rising) and let rise for 40 minutes.",
        "Top with egg white and water mixture, bake for 15 minutes.",
    )


default_recipe_registry.add_recipe(recipe=KaiserRoll())
