from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class CobblerTopping(Recipe):
    name: str = "Cobbler Topping"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=0.3333333333333333, unit="cup", name="butter"),
        MeasurementRegistry.get_measurement(amount=0.16666666666666666, unit="cup", name="white sugar"),
        MeasurementRegistry.get_measurement(amount=0.16666666666666666, unit="cup", name="brown sugar"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="egg", name=""),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="vanilla"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="cup", name="flour"),
        MeasurementRegistry.get_measurement(amount=0.125, unit="tsp.", name="baking powder"),
        MeasurementRegistry.get_measurement(amount=0.125, unit="tsp.", name="salt"),
    ]
    instructions: list[str] = [
        "Cream butter and sugar until light and fluffy.",
        "Mix flour, baking powder, and salt in separate bowl.",
        "Slowly incorporate flour mixture into butter mixture, until just combined.",
        "Drop spoonfuls onto wet mixture.",
        "Bake for 40 min at 375° F.",
    ]


default_recipe_registry.add_recipe(recipe=CobblerTopping())
