from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class ButtermilkWaffles(Recipe):
    name: str = "Buttermilk Waffles"
    tags: tuple[str, ...] = ("American", "Breakfast", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=5 / 2, unit="tbsp", ingredient_name="melted and cooled butter"),
        IngredientRegistry.get_measurement(amount=1, unit="large", ingredient_name="egg"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="buttermilk"),
        IngredientRegistry.get_measurement(amount=1 / 3, unit="tsp", ingredient_name="vanilla extract"),
        IngredientRegistry.get_measurement(amount=60, unit="grams", ingredient_name="flour"),
        IngredientRegistry.get_measurement(amount=2 / 3, unit="tsp", ingredient_name="baking powder"),
        IngredientRegistry.get_measurement(amount=1 / 3, unit="tsp", ingredient_name="baking soda"),
        IngredientRegistry.get_measurement(amount=1 / 3, unit="tsp", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=1 / 6, unit="tsp", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp", ingredient_name="pearl sugar"),
    )
    instructions: tuple[str, ...] = (
        "Waffle will be best if all ingredients are at room temperature",
        "Heat waffle iron.",
        "In a large bowl, combine all dry ingredients. Create a depression for the buttermilk mixture.",
        "Beat the eggs in a large measuring cup until frothy. Add vanilla extract, buttermilk, and cooled melted butter. Beat until well combined.",
        "Pour into the depression and stir quickly but gently with a wooden spoon.",
        "[Experimental]: Gently incorporate pearl sugar.",
        "Use about 1/4 of batter per waffle. Cook until steam stops rising from the iron.",
    )


default_recipe_registry.add_recipe(recipe=ButtermilkWaffles())
