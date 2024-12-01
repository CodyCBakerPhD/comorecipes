from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class BuffaloWings(Recipe):
    name: str = "Buffalo Wings"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=8, unit="separated", name="chicken wings"),
        MeasurementRegistry.get_measurement(amount=2, unit="tsp.", name="salt and pepper"),
        MeasurementRegistry.get_measurement(amount=2, unit="tbsp.", name="butter"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="white vinegar"),
        MeasurementRegistry.get_measurement(amount=100, unit="ml", name="hot sauce of choice"),
    )
    instructions: tuple[str, ...] = (
        "Heat oil to 375 F.",
        "Fry chicken wings for ~10 minutes.",
        "Drain and then toss with salt and pepper.",
        "In a wok, melt butter then add other wet ingredients.",
        "Reduce slightly then toss chicken wings in mixture.",
    )


default_recipe_registry.add_recipe(recipe=BuffaloWings())
