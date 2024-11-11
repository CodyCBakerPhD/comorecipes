from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class BuffaloWings(Recipe):
    name: str = "Buffalo Wings"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=8.0, unit="separated", name="chicken wings"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tsp.", name="salt and pepper"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tbsp.", name="butter"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="white vinegar"),
        MeasurementRegistry.get_measurement(amount=100.0, unit="ml", name="hot sauce of choice"),
    ]
    instructions: list[str] = [
        "Heat oil to 375 °F.",
        "Fry chicken wings for ~10 minutes.",
        "Drain and then toss with salt and pepper.",
        "In a wok, melt butter then add other wet ingredients.",
        "Reduce slightly then toss chicken wings in mixture.",
    ]


default_recipe_registry.add_recipe(recipe=BuffaloWings())
