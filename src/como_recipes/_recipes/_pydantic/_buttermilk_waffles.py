from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class ButtermilkWaffles(Recipe):
    name: str = "Buttermilk Waffles"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=2.5, unit="tbsp.", name="melted and cooled butter"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="large", name="egg"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="buttermilk"),
        MeasurementRegistry.get_measurement(amount=0.3333333333333333, unit="tsp.", name="vanilla extract"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="all-purpose flour"),
        MeasurementRegistry.get_measurement(amount=0.6666666666666666, unit="tsp.", name="baking powder"),
        MeasurementRegistry.get_measurement(amount=0.3333333333333333, unit="tsp.", name="baking soda"),
        MeasurementRegistry.get_measurement(amount=0.3333333333333333, unit="tsp.", name="sugar"),
        MeasurementRegistry.get_measurement(amount=0.16666666666666666, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="pearl sugar"),
    ]
    instructions: list[str] = [
        "Waffle will be best if all ingredients are at room temperature",
        "Heat waffle iron.",
        "In a large bowl, combine all dry ingredients. Create a depression for the buttermilk mixture.",
        "Beat the eggs in a large measuring cup until frothy. Add vanilla extract, buttermilk, and cooled melted butter. Beat until well combined.",
        "Pour into the depression and stir quickly but gently with a wooden spoon.",
        "[Experimental]: Gently incorporate pearl sugar.",
        "Use about 1/4 of batter per waffle. Cook until steam stops rising from the iron.",
    ]


default_recipe_registry.add_recipe(recipe=ButtermilkWaffles())
