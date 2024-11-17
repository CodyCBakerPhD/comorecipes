from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class Sourdough(Recipe):
    name: str = "Sourdough"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=260.0, unit="g.", name="bread flour"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=60.0, unit="g.", name="yeast start"),
        MeasurementRegistry.get_measurement(amount=200.0, unit="g.", name="water"),
    ]
    instructions: list[str] = [
        "Begin process the morning of the day before intended dinner.",
        "Mix flour and salt.",
        "Mix yeast into water until cloudy.",
        "Combine wet and dry mixtures with a fork to start, then wooden spoon.",
        "Gently fold 2-3 times every 15 minutes.",
        "Let rise at room temperature all day.",
        "Refridgerate overnight. Slash scores into the top of dough before baking.",
        "Bake in dutch oven covered for 20 minutes 500° F, then uncover for another 10-15 minutes.",
    ]


default_recipe_registry.add_recipe(recipe=Sourdough())
