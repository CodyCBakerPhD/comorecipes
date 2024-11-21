from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class BananaBread(Recipe):
    name: str = "Banana Bread"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=0.25, unit="cup", name="butter"),
        MeasurementRegistry.get_measurement(amount=0.125, unit="cup", name="sugar"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="egg", name=""),
        MeasurementRegistry.get_measurement(amount=1.0, unit="ripe", name="banana"),
        MeasurementRegistry.get_measurement(amount=0.125, unit="tsp.", name="of salt"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="baking soda"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="flour"),
    )
    instructions: tuple[str, ...] = (
        "Preheat oven to 300 F.",
        "Cream butter and sugar.",
        "Combine all dry ingredients and mix well.",
        "Combine all remaining ingredients and mix well.",
        "Bake for 35 minutes.",
    )


default_recipe_registry.add_recipe(recipe=BananaBread())
