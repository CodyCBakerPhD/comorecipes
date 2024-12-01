from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class NutellaBites(Recipe):
    name: str = "Nutella Bites"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=3 / 2, unit="", name="cups oats"),
        MeasurementRegistry.get_measurement(amount=2 / 3, unit="", name="cup Nutella"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="", name="cu. shredded coconut"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="", name="cup honey"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="", name="cup roasted hazelnuts"),
        MeasurementRegistry.get_measurement(amount=2, unit="", name="tsp. vanilla extract"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="", name="tsp. salt"),
    )
    instructions: tuple[str, ...] = (
        "Combine all ingredients in large bowl and mix thoroughly.",
        "Cover and put in refrigerator for 30-60 minutes to make texture easier to mold.",
        "Roll balls of desired size and keep refrigerated.",
    )


default_recipe_registry.add_recipe(recipe=NutellaBites())
