from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class VegetarianGravy(Recipe):
    name: str = "Vegetarian Gravy"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=0.25, unit="cup", name="butter"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="cup", name="flour"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="cups", name="not-chicken stock"),
        MeasurementRegistry.get_measurement(amount=0.3333333333333333, unit="cup", name="heavy cream"),
        MeasurementRegistry.get_measurement(amount=1.25, unit="tsp.", name="salt and pepper"),
        MeasurementRegistry.get_measurement(amount=0.16666666666666666, unit="tsp.", name="paprika"),
    ]
    instructions: list[str] = [
        "Make roux with butter and flour. Thicken with stock. Season.",
    ]


default_recipe_registry.add_recipe(recipe=VegetarianGravy())
