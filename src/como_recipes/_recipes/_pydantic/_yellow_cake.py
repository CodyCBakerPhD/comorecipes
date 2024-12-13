from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class YellowCake(Recipe):
    name: str = "Yellow Cake"
    tags: tuple[str, ...] = ("American", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="cup", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=3 / 2, unit="cup", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=8, unit="egg", ingredient_name="yolks"),
        IngredientRegistry.get_measurement(amount=3 / 4, unit="cup", ingredient_name="milk"),
        IngredientRegistry.get_measurement(amount=3 / 2, unit="tsp.", ingredient_name="vanilla"),
        IngredientRegistry.get_measurement(amount=2, unit="cups", ingredient_name="cake flour"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp.", ingredient_name="baking powder"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", ingredient_name="salt"),
    )
    instructions: tuple[str, ...] = (
        "Preheat to 350 F. Grease cake pan or cupcake pan.",
        "Sift together flour, baking powder, and salt.",
        "In separate bowl, cream butter and sugar until light and fluffy.",
        "Beat in egg yolks one at a time, then stir in the vanilla.",
        "Beat in the flour mixture alternately with the milk, mixing just until incorporated.",
        "Pour batter into pan. Bake for 25-30 minutes.",
        "Cool 15 minutes before turning out onto rack or plate.",
    )


default_recipe_registry.add_recipe(recipe=YellowCake())
