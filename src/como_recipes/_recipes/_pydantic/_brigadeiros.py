from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class Brigadeiros(Recipe):
    name: str = "Brigadeiros"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=3.0, unit="tbsp.", name="unsweetened cocoa"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="butter"),
        MeasurementRegistry.get_measurement(amount=14.0, unit="oz.", name="condensed milk"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="chocolate sprinkles"),
    ]
    instructions: list[str] = [
        "Combine cocoa, butter, and condensed milk in a medium saucepan over medium heat.",
        "Cook and stir until thickened, about 10 minutes.",
        "Remove from heat and let rest until just cool enough to handle.",
        "Form into small balls and coat with sprinkles.",
    ]


default_recipe_registry.add_recipe(recipe=Brigadeiros())
