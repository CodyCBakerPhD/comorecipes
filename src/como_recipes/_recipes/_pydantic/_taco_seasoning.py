from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class TacoSeasoning(Recipe):
    name: str = "Taco Seasoning"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="", name="tsp. garlic powder"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="", name="tsp. onion powder"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="", name="tsp. red pepper"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="", name="tsp. dried oregano"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="", name="tsp. paprika"),
        MeasurementRegistry.get_measurement(amount=3 / 2, unit="tsp.", name="cumin"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="", name="tsp. salt"),
        MeasurementRegistry.get_measurement(amount=1, unit="", name="tsp. pepper"),
        MeasurementRegistry.get_measurement(amount=1, unit="", name="lb. ground beef or refried beans or Boca"),
    )
    instructions: tuple[str, ...] = (
        "Mix spice.",
        "To use spice to make tacos, brown beef or boca.",
        "Add mix and some water for incorporation (beef or Boca).",
        "Cook off excess water to allow base to absorb spice.",
    )


default_recipe_registry.add_recipe(recipe=TacoSeasoning())
