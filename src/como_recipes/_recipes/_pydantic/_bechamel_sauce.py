from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class BechamelSauce(Recipe):
    name: str = "Bechamel Sauce"
    measurements: tuple[Measurement] = (
        MeasurementRegistry.get_measurement(amount=2.0, unit="tbsp.", name="butter"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tbsp.", name="flour"),
        MeasurementRegistry.get_measurement(amount=1.25, unit="cup", name="whole milk"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="salt and pepper"),
    )
    instructions: tuple[str] = ("Make roux with butter and flour. Thicken with milk. Season.",)


default_recipe_registry.add_recipe(recipe=BechamelSauce())
