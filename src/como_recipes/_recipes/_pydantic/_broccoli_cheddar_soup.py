from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class BroccoliCheddarSoup(Recipe):
    name: str = "Broccoli Cheddar Soup"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=0.25, unit="cup", name="butter"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="onion", name=""),
        MeasurementRegistry.get_measurement(amount=8.0, unit="oz.", name="broccoli"),
        MeasurementRegistry.get_measurement(amount=7.0, unit="oz.", name="not-chicken broth"),
        MeasurementRegistry.get_measurement(amount=8.0, unit="oz.", name="cheddar"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="milk"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tbsp.", name="garlic powder"),
        MeasurementRegistry.get_measurement(amount=0.125, unit="cup", name="cornstarch"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="water"),
    )
    instructions: tuple[str, ...] = (
        "In pot, melt butter over medium heat. Cook onion until softened. Stir in broccoli and cover with not-chicken broth. Simmer until tender, 10-15 minutes.",
        "Reduce heat and stir in cheese cubes until melted. Mix in milk and garlic powder. In a small bowl, stir cornstarch into water until dissolved.",
        "Stir mixture into soup, cook, stirring frequently, until thick.",
    )


default_recipe_registry.add_recipe(recipe=BroccoliCheddarSoup())
