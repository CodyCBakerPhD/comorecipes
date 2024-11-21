from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class PumpkinPieFilling(Recipe):
    name: str = "Pumpkin Pie Filling"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=15.0, unit="oz.", name="fresh pumpkin puree"),
        MeasurementRegistry.get_measurement(amount=14.0, unit="oz.", name="condensed milk"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="eggs", name=""),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="ginger"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="nutmeg"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="pie", name="crust"),
    )
    instructions: tuple[str, ...] = ("Mix ingredients well and pour into pie crust. Bake for 15 minutes at 425 F.",)


default_recipe_registry.add_recipe(recipe=PumpkinPieFilling())
