from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class KaiserRoll(Recipe):
    name: str = "Kaiser Roll"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="water"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="yeast"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="sugar or honey"),
        MeasurementRegistry.get_measurement(amount=0.16666666666666666, unit="cup", name="vegetable oil"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="cups", name="flour"),
    ]
    instructions: list[str] = [
        "Preheat oven to 400 °F. Activate yeast.",
        "Mix in oil and flour and salt until good consistency. Roll out into shape (make sure the rolls are appropriately sized for rising) and let rise for 40 minutes.",
        "Top with egg white and water mixture, bake for 15 minutes.",
    ]


default_recipe_registry.add_recipe(recipe=KaiserRoll())
