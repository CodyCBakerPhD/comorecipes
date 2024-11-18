from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class WhippedCreamCheeseFilling(Recipe):
    name: str = "Whipped Cream Cheese Filling"
    measurements: tuple[Measurement] = (
        MeasurementRegistry.get_measurement(amount=1.0, unit="", name="cup heavy cream"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="", name="cup powdered sugar"),
        MeasurementRegistry.get_measurement(amount=3.0, unit="", name="oz cream cheese"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="", name="tsp vanilla extract"),
    )
    instructions: tuple[str] = (
        "Chill whisk and bowl for stand mixer.",
        "Add all ingredients at once and mix on high until stiff peaks form.",
    )


default_recipe_registry.add_recipe(recipe=WhippedCreamCheeseFilling())
