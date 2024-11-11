from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class EnchiladaBeef(Recipe):
    name: str = "Enchilada Beef"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=24.0, unit="oz.", name="chuck roast"),
        MeasurementRegistry.get_measurement(amount=3.0, unit="tbsp.", name="flour"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tbsp.", name="extra virgin olive oil"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="black pepper"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="water"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="beef concentrate"),
    ]
    instructions: list[str] = [
        "Dredge meat in flour and pepper. Brown in skillet.",
        "Heat water to simmer, add beef concentrate.",
        "Combine in crockpot, set to high for 1 hour. Turn to low for 6-7 hours.",
    ]


default_recipe_registry.add_recipe(recipe=EnchiladaBeef())
