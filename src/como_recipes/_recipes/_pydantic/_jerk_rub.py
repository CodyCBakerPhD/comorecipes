from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class JerkRub(Recipe):
    name: str = "Jerk Rub"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="garlic powder"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="cumin"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="coriander"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="paprika"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="salt and pepper"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="olive oil"),
    ]
    instructions: list[str] = [
        "Mix dry ingredients and use oil to bind. For cooking with chicken, lather all sides and grill for 4-6 minutes on each side.",
    ]


default_recipe_registry.add_recipe(recipe=JerkRub())
