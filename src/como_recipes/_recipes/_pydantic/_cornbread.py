from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class Cornbread(Recipe):
    name: str = "Cornbread"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="cup", name="butter"),
        MeasurementRegistry.get_measurement(amount=1 / 6, unit="cup", name="sugar"),
        MeasurementRegistry.get_measurement(amount=1, unit="large", name="egg"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="buttermilk"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="baking soda"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="cornmeal"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="flour"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="salt"),
    )
    instructions: tuple[str, ...] = (
        "Preheat to 375 F. Melt butter. Stir in sugar. Add eggs, beat.",
        "Combine buttermilk and soda, stir into mixture.",
        "Add remaining ingredients, stir until blended.",
        "Bake for about 20 minutes, until slightly brown on top.",
    )


default_recipe_registry.add_recipe(recipe=Cornbread())
