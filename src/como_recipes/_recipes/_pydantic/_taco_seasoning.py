from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class TacoSeasoning(Recipe):
    name: str = "Taco Seasoning"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=0.25, unit="", name="tsp. garlic powder"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="", name="tsp. onion powder"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="", name="tsp. red pepper"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="", name="tsp. dried oregano"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="", name="tsp. paprika"),
        MeasurementRegistry.get_measurement(amount=1.5, unit="tsp.", name="cumin"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="", name="tsp. salt"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="", name="tsp. pepper"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="", name="lb. ground beef or refried beans or Boca"),
    ]
    instructions: list[str] = [
        "Mix spice.",
        "To use spice to make tacos, brown beef or boca.",
        "Add mix and some water for incorporation (beef or Boca).",
        "Cook off excess water to allow base to absorb spice.",
    ]


default_recipe_registry.add_recipe(recipe=TacoSeasoning())
