from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class SloppyJoes(Recipe):
    name: str = "Sloppy Joes"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=1.0, unit="batch", name="of Kaiser Rolls"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="lb", name="ground beef or Boca crumbles"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="cup", name="red onion"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="garlic powder"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tsp.", name="yellow mustard"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="ketchup"),
        MeasurementRegistry.get_measurement(amount=3.0, unit="tsp.", name="brown sugar"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tbsp.", name="molasses"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="salt and pepper"),
    ]
    instructions: list[str] = [
        "Brown meat. Mix spices. Simmer until good consistency.",
    ]


default_recipe_registry.add_recipe(recipe=SloppyJoes())
