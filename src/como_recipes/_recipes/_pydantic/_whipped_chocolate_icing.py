from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class WhippedChocolateIcing(Recipe):
    name: str = "Whipped Chocolate Icing"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=2.75, unit="cups", name="sifted powdered sugar"),
        MeasurementRegistry.get_measurement(amount=6.0, unit="tbsp.", name="cocoa powder"),
        MeasurementRegistry.get_measurement(amount=6.0, unit="tbsp.", name="room-temperature butter"),
        MeasurementRegistry.get_measurement(amount=5.0, unit="tbsp.", name="evaporated milk"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="vanilla extract"),
    ]
    instructions: list[str] = [
        "Sift the cocoa powder and powdered sugar together.",
        "In a separate bowl, cream butter until smooth and gradually beat in sugar and evaporated milk.",
        "Blend in vanilla.",
        "Beat until light and fluffy.",
    ]


default_recipe_registry.add_recipe(recipe=WhippedChocolateIcing())
