from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class SimpleCaramel(Recipe):
    name: str = "Simple Caramel"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=14.0, unit="oz.", name="sweetened condensed milk"),
        MeasurementRegistry.get_measurement(amount=7.0, unit="tbsp.", name="butter, cut into pieces"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="brown sugar"),
        MeasurementRegistry.get_measurement(amount=0.16666666666666666, unit="cup", name="light corn syrup"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="vanilla extract"),
        MeasurementRegistry.get_measurement(amount=0.125, unit="tsp.", name="salt"),
    ]
    instructions: list[str] = [
        "Combine condensed milk, butter, brown sugar, and corn syrup in medium saucepan over medium heat.",
        "Stir frequently until butter is melted and ingredients are combined.",
        "Continue to constantly stir until mixture begins to boil.",
        "Once mixture begins to boil, reduce heat to simmer and continue to stir.",
        "Continue for 8-10 minutes until mixture has thickened and darkened.",
        "Remove from heat and immediately mix in vanilla extract and salt.",
    ]


default_recipe_registry.add_recipe(recipe=SimpleCaramel())
