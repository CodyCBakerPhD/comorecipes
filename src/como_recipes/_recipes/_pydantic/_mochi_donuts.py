from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class MochiDonuts(Recipe):
    name: str = "Mochi Donuts"
    measurements: tuple[Measurement] = (
        MeasurementRegistry.get_measurement(amount=150.0, unit="grams", name="mochiko"),
        MeasurementRegistry.get_measurement(amount=50.0, unit="grams", name="brown sugar"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp", name="baking powder"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp", name="salt"),
        MeasurementRegistry.get_measurement(amount=50.0, unit="grams", name="melted butter"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="large", name="egg"),
        MeasurementRegistry.get_measurement(amount=200.0, unit="grams", name="whole milk"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp", name="vanilla"),
    )
    instructions: tuple[str] = (
        "Preheat to 350. grease pan.",
        "Combine dry ingredients, whisk together.",
        "Combine wet ingredients.",
        "Combine dry and wet ingredients until smooth.",
        "Bake for 25-30 minutes.",
        "Let cool for 5-10 minutes before icing.",
    )


default_recipe_registry.add_recipe(recipe=MochiDonuts())
