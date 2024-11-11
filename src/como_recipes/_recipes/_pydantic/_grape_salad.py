from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class GrapeSalad(Recipe):
    name: str = "Grape Salad"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=8.0, unit="oz.", name="cream cheese, softened"),
        MeasurementRegistry.get_measurement(amount=8.0, unit="oz.", name="sour cream"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tsp", name="vanilla extract"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="lb", name="red seedless grapes"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="lbs", name="green seedless grapes"),
        MeasurementRegistry.get_measurement(amount=3.0, unit="tbsp", name="brown sugar"),
        MeasurementRegistry.get_measurement(amount=3.0, unit="tbsp", name="chopped pecans"),
    ]
    instructions: list[str] = [
        "In a large bowl, beat the cream cheese, sour cream, sugar and vanilla until blended. Add grapes and toss to coat.",
        "Transfer to a serving bowl. Cover and refrigerate until serving. Sprinkle with brown sugar and pecans just before serving",
        "Note: Makes 21-24 servings",
    ]


default_recipe_registry.add_recipe(recipe=GrapeSalad())
