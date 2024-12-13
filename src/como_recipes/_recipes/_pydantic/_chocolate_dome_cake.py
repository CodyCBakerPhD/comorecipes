from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class ChocolateDomeCake(Recipe):
    name: str = "Chocolate Dome Cake"
    tags: tuple[str, ...] = ("American", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=4, unit="large", ingredient_name="eggs"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=3 / 4, unit="cup", ingredient_name="cake flour"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", ingredient_name="whipping cream"),
        IngredientRegistry.get_measurement(amount=5, unit="oz.", ingredient_name="semi-sweet chocolate"),
        IngredientRegistry.get_measurement(amount=7, unit="oz.", ingredient_name="high-quality chocolate for coating"),
        IngredientRegistry.get_measurement(amount=1, unit="1/2", ingredient_name="cup raspberries"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", ingredient_name="lime juice"),
    )
    instructions: tuple[str, ...] = (
        "Preheat to 350 F. Whip eggs and sugar until thick and frothy. Fold in flour. Bake in round bowl for 1 hour.",
        "Whip cream, fold in melted chocolate.",
        "Slice cake into three layers and fill evenly with mousse. Lay saran wrap large and flat enough to cover the surface of the cake.",
        "Melt milk chocolate and delicately spread on saran wrap. Carefully move into the bowl used to bake the cake, and gently place cake back in the bowl.",
        "Refrigerate until chocolate has bound and solidified.",
        "Blend sauce ingredients, keep cold until served.",
    )


default_recipe_registry.add_recipe(recipe=ChocolateDomeCake())
