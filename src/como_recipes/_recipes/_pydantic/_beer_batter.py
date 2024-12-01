from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class BeerBatter(Recipe):
    name: str = "Beer Batter"
    tags: tuple[str, ...] = "American"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=2, unit="cups", name="flour"),
        MeasurementRegistry.get_measurement(amount=1 / 3, unit="cup", name="cornstarch"),
        MeasurementRegistry.get_measurement(amount=2, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="paprika"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="baking powder"),
        MeasurementRegistry.get_measurement(amount=12, unit="oz.", name="beer"),
    )
    instructions: tuple[str, ...] = (
        "Whisk dry ingredients. Add beer and incorporate. Mixture should feel like pancake batter.",
        "Cook 2-3 minutes per side in 375 F oil.",
    )


default_recipe_registry.add_recipe(recipe=BeerBatter())
