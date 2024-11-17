from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class BakedPotato(Recipe):
    name: str = "Baked Potato"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=4.0, unit="Good", name="big potatoes"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="olive oil"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="large-grain salt"),
    ]
    instructions: list[str] = [
        "Use aluminum foil for easy cleanup.",
        "Thoroughly scrub potatoes.",
        "Cut into quarters lengthwise.",
        "Rub all over with peanut oil and coat with a bit of large-grain salt.",
        "Bake for 45 min at 425° F.",
    ]


default_recipe_registry.add_recipe(recipe=BakedPotato())
