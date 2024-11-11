from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class KeyLimeFilling(Recipe):
    name: str = "Key Lime Filling"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=28.0, unit="oz.", name="sweetened condensed milk"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="sour cream"),
        MeasurementRegistry.get_measurement(amount=0.75, unit="cup", name="Key lime juice"),
    ]
    instructions: list[str] = [
        "Mix.",
        "Eat as pudding by dipping Graham crackers in it, or bake in Graham cracker crust for about 10 minutes at 350 °F.",
    ]


default_recipe_registry.add_recipe(recipe=KeyLimeFilling())
