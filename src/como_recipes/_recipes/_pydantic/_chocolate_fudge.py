from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class ChocolateFudge(Recipe):
    name: str = "Chocolate Fudge"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian", "Chocolate")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="lb.", ingredient_name="powdered sugar"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="dutch cocoa powder"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="chocolate milk"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="vanilla"),
        IngredientRegistry.get_measurement(
            amount=1 / 2,
            unit="cup",
            ingredient_name="chopped walnuts or pecans, optional",
        ),
    )
    instructions: tuple[str, ...] = (
        "One of several variations on chocolate fudge.",
        "Line a 6 x 8 pan with parchment paper misted very lightly with cooking spray.",
        "Sift powdered sugar and cocoa powder. Cube butter into 1 inch chunks.",
        "Pour an inch or two of water into a saucepan, then bring to a simmer.",
        "Place powdered sugar, cocoa powder, butter, and milk into a large bowl, then place the bowl on top of the saucepan with simmering water.",
        "Cook, whisking regularly, until the butter has melted, and the mixture is smooth.",
        "Remove from heat, stir in the vanilla and optional chopped nuts, then pour quickly into prepared pan.",
        "Chill until solidified.",
    )


default_recipe_registry.add_recipe(recipe=ChocolateFudge())
