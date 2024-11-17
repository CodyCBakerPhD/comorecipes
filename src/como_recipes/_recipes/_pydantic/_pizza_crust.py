from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class PizzaCrust(Recipe):
    name: str = "Pizza Crust"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="water"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="yeast"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="sugar or honey"),
        MeasurementRegistry.get_measurement(amount=9.0, unit="oz.", name="flour"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="salt"),
    ]
    instructions: list[str] = [
        "Activate yeast. Mix in flour and salt until good consistency. Knead for 3 minutes. Place in oiled rising container. Set timer for 40 minutes and let rise in warm spot.",
        "Preheat oven to 400 F. Press into shape and top. Brush sides with truffle oil and seasoning. Bake for around 13 minutes.",
    ]


default_recipe_registry.add_recipe(recipe=PizzaCrust())
