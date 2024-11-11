from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class FryingBreading(Recipe):
    name: str = "Frying Breading"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=6.0, unit="cups", name="all-purpose flour"),
        MeasurementRegistry.get_measurement(amount=10.0, unit="tbsp.", name="salt and pepper"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tbsp.", name="garlic powder"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="onion powder"),
        MeasurementRegistry.get_measurement(amount=4.0, unit="tsp.", name="cayenne pepper"),
    ]
    instructions: list[str] = [
        "Mix in large batches and store for later use.",
    ]


default_recipe_registry.add_recipe(recipe=FryingBreading())
