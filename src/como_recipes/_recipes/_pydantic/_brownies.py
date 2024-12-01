from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class Brownies(Recipe):
    name: str = "Brownies"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="vegetable oil"),
        MeasurementRegistry.get_measurement(amount=2 / 3, unit="cup", name="sugar"),
        MeasurementRegistry.get_measurement(amount=2, unit="large", name="eggs"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="vanilla"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="baking powder"),
        MeasurementRegistry.get_measurement(amount=1 / 3, unit="cup", name="cocoa powder"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="flour"),
        MeasurementRegistry.get_measurement(amount=3, unit="tbsp.", name="chocolate chips"),
    )
    instructions: tuple[str, ...] = (
        "Preheat to 350 F, spray pan.",
        "Mix oil and sugar well.",
        "Add eggs and vanilla, just barely blend in.",
        "Mix all dry ingredients separately, stir into oil mixture.",
        "Bake around 20 minutes.",
    )


default_recipe_registry.add_recipe(recipe=Brownies())
