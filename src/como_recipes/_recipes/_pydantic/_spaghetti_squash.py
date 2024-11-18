from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class SpaghettiSquash(Recipe):
    name: str = "Spaghetti Squash"
    measurements: tuple[Measurement] = (
        MeasurementRegistry.get_measurement(amount=1.0, unit="spaghetti", name="squash"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="olive oil"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="salt and pepper"),
    )
    instructions: tuple[str] = (
        "Cut and clean inside of squash.",
        "Coat with oil and season.",
        "Place face down on baking sheet lined with aluminum foil.",
        "Bake for 40 minutes at 375 °F.",
    )


default_recipe_registry.add_recipe(recipe=SpaghettiSquash())
