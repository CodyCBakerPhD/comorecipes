from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class ExampleRecipe1(Recipe):
    name: str = "Example Recipe 1"
    measurements: tuple[Measurement] = (
        MeasurementRegistry.get_measurement(amount=3.0, unit="tbsp.", name="ingredient 1"),
        MeasurementRegistry.get_measurement(amount=4.0, unit="g", name="ingredient 2"),
    )
    instructions: tuple[str] = ("This is an example of a recipe.",)


default_recipe_registry.add_recipe(recipe=ExampleRecipe1())
