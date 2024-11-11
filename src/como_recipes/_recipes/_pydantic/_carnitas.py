from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class Carnitas(Recipe):
    name: str = "Carnitas"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=1.0, unit="lb.", name="pork shoulder"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="oregano"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tsp.", name="cumin"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="chili powder"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="flour"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="salt and pepper"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="oranges,", name="juiced"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="cloves", name="minced garlic"),
    ]
    instructions: list[str] = [
        "Brown pork with dry spices rubbed in. Slow cook in other ingredients for 6-8 hours on low in a small slow-cooker.",
        "Remove and shred, reserving strained liquid. Crisp in large skillet with remaining juices until evaporated.",
    ]


default_recipe_registry.add_recipe(recipe=Carnitas())
