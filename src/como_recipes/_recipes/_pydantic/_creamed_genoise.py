from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class CreamedGenoise(Recipe):
    name: str = "Creamed Genoise"
    tags: tuple[str, ...] = ("British", "Dessert", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=375 / 2, unit="g.", ingredient_name="butter, room temperature"),
        IngredientRegistry.get_measurement(amount=375 / 2, unit="g.", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=3, unit="", ingredient_name="beaten eggs, room temperature"),
        IngredientRegistry.get_measurement(amount=187, unit="grams", ingredient_name="cake flour"),
        IngredientRegistry.get_measurement(amount=1, unit="", ingredient_name="tsp. baking powder"),
        IngredientRegistry.get_measurement(amount=25, unit="ml.", ingredient_name="milk"),
        IngredientRegistry.get_measurement(amount=1, unit="", ingredient_name="tsp. vanilla extract"),
    )
    instructions: tuple[str, ...] = (
        "Preheat to 350 F.",
        "Cream butter and sugar with wooden spoon, then set in stand mixer on medium-high for about two minutes, constantly scraping the sides.",
        "Then begin adding very small drizzle of the egg into the butter mixture while it remains in the stand mixer on medium-high. Continue until all egg is incorporated.",
        "Now remove from stand mixer and over the course of several gentle folds, sift and incorporate the flour and baking powder.",
        "Halfway through the folding, add half the milk/vanilla mixture. Add remaining at the end.",
        "Bake for around 20 minutes.",
    )


default_recipe_registry.add_recipe(recipe=CreamedGenoise())
