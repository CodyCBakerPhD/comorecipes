from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class KaiserRoll(Recipe):
    name: str = "Kaiser Roll"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1, unit="cup", name="water"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="yeast"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="sugar or honey"),
        MeasurementRegistry.get_measurement(amount=1 / 6, unit="cup", name="vegetable oil"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=2, unit="cups", name="flour"),
    )
    instructions: tuple[str, ...] = (
        "Preheat oven to 400 F. Activate yeast.",
        "Mix in oil and flour and salt until good consistency. Roll out into shape (make sure the rolls are appropriately sized for rising) and let rise for 40 minutes.",
        "Top with egg white and water mixture, bake for 15 minutes.",
    )


default_recipe_registry.add_recipe(recipe=KaiserRoll())
