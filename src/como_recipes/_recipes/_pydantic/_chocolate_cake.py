from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class ChocolateCake(Recipe):
    name: str = "Chocolate Cake"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1, unit="cup", name="flour"),
        MeasurementRegistry.get_measurement(amount=1, unit="cup", name="sugar"),
        MeasurementRegistry.get_measurement(amount=3 / 8, unit="cup", name="cocoa powder"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="baking powder"),
        MeasurementRegistry.get_measurement(amount=3 / 4, unit="tsp.", name="baking soda"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="espresso powder"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="milk"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="cup", name="vegetable oil"),
        MeasurementRegistry.get_measurement(amount=1, unit="large", name="egg"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="vanilla"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="boiling water"),
    )
    instructions: tuple[str, ...] = (
        "Preheat to 350 F. Spray pan.",
        "Add all dry ingredients and mix. Boil water.",
        "Add non-water wet ingredients and mix until well combined. Reduce speed and carefully add boiling water and mix well.",
        "Immediately transfer mixture to pan and bake for 30-35 minutes.",
    )


default_recipe_registry.add_recipe(recipe=ChocolateCake())
