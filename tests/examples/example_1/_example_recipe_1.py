from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class ExampleRecipe1(Recipe):
    name: str = "Example Recipe 1"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=3.0, unit="tbsp.", name="ingredient 1"),
        MeasurementRegistry.get_measurement(amount=4.0, unit="g", name="ingredient 2"),
    ]
    instructions: list[str] = [
        "This is an example of a recipe.",
    ]


default_recipe_registry.add_recipe(recipe=ExampleRecipe1())
