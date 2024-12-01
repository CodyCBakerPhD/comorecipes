from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class WhippedChocolateIcing(Recipe):
    name: str = "Whipped Chocolate Icing"
    tags: tuple[str, ...] = "American"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=11 / 4, unit="cups", name="sifted powdered sugar"),
        MeasurementRegistry.get_measurement(amount=6, unit="tbsp.", name="cocoa powder"),
        MeasurementRegistry.get_measurement(amount=6, unit="tbsp.", name="room-temperature butter"),
        MeasurementRegistry.get_measurement(amount=5, unit="tbsp.", name="evaporated milk"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="vanilla extract"),
    )
    instructions: tuple[str, ...] = (
        "Sift the cocoa powder and powdered sugar together.",
        "In a separate bowl, cream butter until smooth and gradually beat in sugar and evaporated milk.",
        "Blend in vanilla.",
        "Beat until light and fluffy.",
    )


default_recipe_registry.add_recipe(recipe=WhippedChocolateIcing())
