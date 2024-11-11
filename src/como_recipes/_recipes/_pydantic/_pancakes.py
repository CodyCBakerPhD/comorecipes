from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class Pancakes(Recipe):
    name: str = "Pancakes"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=1.0, unit="", name="cup flour"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="", name="tbsp. sugar"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="", name="tsp. baking powder"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="", name="tsp. baking soda"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="", name="tsp. salt"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="", name="egg"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="", name="tbsp. butter"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="", name="cup buttermilk"),
    ]
    instructions: list[str] = [
        "Combine dry ingredients.",
        "Melt butter, mix with egg and buttermilk; whisk well.",
        "Cook on griddle.",
    ]


default_recipe_registry.add_recipe(recipe=Pancakes())
