from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class BeerBatter(Recipe):
    name: str = "Beer Batter"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=2.0, unit="cups", name="flour"),
        MeasurementRegistry.get_measurement(amount=0.3333333333333333, unit="cup", name="cornstarch"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="paprika"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="baking powder"),
        MeasurementRegistry.get_measurement(amount=12.0, unit="oz.", name="beer"),
    )
    instructions: tuple[str, ...] = (
        "Whisk dry ingredients. Add beer and incorporate. Mixture should feel like pancake batter.",
        "Cook 2-3 minutes per side in 375 F oil.",
    )


default_recipe_registry.add_recipe(recipe=BeerBatter())
