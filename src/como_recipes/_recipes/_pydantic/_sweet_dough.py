from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class SweetDough(Recipe):
    name: str = "Sweet Dough"
    measurements: tuple[Measurement] = (
        MeasurementRegistry.get_measurement(amount=0.6666666666666666, unit="cup", name="whole milk"),
        MeasurementRegistry.get_measurement(amount=5.0, unit="tbsp.", name="sugar"),
        MeasurementRegistry.get_measurement(amount=1.75, unit="tsp.", name="yeast"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="eggs,", name="room temperature"),
        MeasurementRegistry.get_measurement(amount=2.75, unit="cups", name="flour"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="butter, room temperature"),
    )
    instructions: tuple[str] = (
        "Heat milk to 110 °F in small saucepan over medium heat.",
        "Stir in 1 tbsp. sugar and yeast.",
        "Let sit for 5 minutes.",
        "Add eggs.",
        "Combine remaining dry ingredients then knead into dough.",
        "Let prove for 90 minutes.",
    )


default_recipe_registry.add_recipe(recipe=SweetDough())
