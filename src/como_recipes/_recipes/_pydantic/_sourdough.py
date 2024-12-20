from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class Sourdough(Recipe):
    name: str = "Sourdough"
    tags: tuple[str, ...] = ("American", "Vegetarian", "Side")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=260, unit="grams", ingredient_name="bread flour"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=60, unit="g.", ingredient_name="yeast start"),
        IngredientRegistry.get_measurement(amount=200, unit="g.", ingredient_name="water"),
    )
    instructions: tuple[str, ...] = (
        "Begin process the morning of the day before intended dinner.",
        "Mix flour and salt.",
        "Mix yeast into water until cloudy.",
        "Combine wet and dry mixtures with a fork to start, then wooden spoon.",
        "Gently fold 2-3 times every 15 minutes.",
        "Let rise at room temperature all day.",
        "Refridgerate overnight. Slash scores into the top of dough before baking.",
        "Bake in dutch oven covered for 20 minutes 500 F, then uncover for another 10-15 minutes.",
    )


default_recipe_registry.add_recipe(recipe=Sourdough())
