from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class ChocolateDoughnutIcing(Recipe):
    name: str = "Chocolate Doughnut Icing"
    measurements: tuple[Measurement] = (
        MeasurementRegistry.get_measurement(amount=0.75, unit="cup", name="powdered sugar"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tbsp.", name="dutch cocoa powder"),
        MeasurementRegistry.get_measurement(amount=0.0625, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tbsp.", name="milk"),
        MeasurementRegistry.get_measurement(amount=0.75, unit="tsp.", name="vanilla"),
    )
    instructions: tuple[str] = (
        "Do not forget to sift dry ingredients.",
        "Combine until smooth in stand mixer.",
        "Spread on doughtnuts immediately.",
    )


default_recipe_registry.add_recipe(recipe=ChocolateDoughnutIcing())
