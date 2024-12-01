from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class ButtermilkWaffles(Recipe):
    name: str = "Buttermilk Waffles"
    tags: tuple[str, ...] = "American"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=5 / 2, unit="tbsp.", name="melted and cooled butter"),
        MeasurementRegistry.get_measurement(amount=1, unit="large", name="egg"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="buttermilk"),
        MeasurementRegistry.get_measurement(amount=1 / 3, unit="tsp.", name="vanilla extract"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="all-purpose flour"),
        MeasurementRegistry.get_measurement(amount=2 / 3, unit="tsp.", name="baking powder"),
        MeasurementRegistry.get_measurement(amount=1 / 3, unit="tsp.", name="baking soda"),
        MeasurementRegistry.get_measurement(amount=1 / 3, unit="tsp.", name="sugar"),
        MeasurementRegistry.get_measurement(amount=1 / 6, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="pearl sugar"),
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
