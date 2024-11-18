from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class Brownies(Recipe):
    name: str = "Brownies"
    measurements: tuple[Measurement] = (
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="vegetable oil"),
        MeasurementRegistry.get_measurement(amount=0.6666666666666666, unit="cup", name="sugar"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="large", name="eggs"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="vanilla"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="baking powder"),
        MeasurementRegistry.get_measurement(amount=0.3333333333333333, unit="cup", name="cocoa powder"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="flour"),
        MeasurementRegistry.get_measurement(amount=3.0, unit="tbsp.", name="chocolate chips"),
    )
    instructions: tuple[str] = (
        "Preheat to 350 °F, spray pan.",
        "Mix oil and sugar well.",
        "Add eggs and vanilla, just barely blend in.",
        "Mix all dry ingredients separately, stir into oil mixture.",
        "Bake around 20 minutes.",
    )


default_recipe_registry.add_recipe(recipe=Brownies())
