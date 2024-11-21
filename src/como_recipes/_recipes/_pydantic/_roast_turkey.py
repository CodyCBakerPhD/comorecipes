from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class RoastTurkey(Recipe):
    name: str = "Roast Turkey"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1, unit="large", name="turkey bag"),
        MeasurementRegistry.get_measurement(amount=8, unit="quarts", name="water"),
        MeasurementRegistry.get_measurement(amount=2, unit="cups", name="Kosher salt"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="brown sugar"),
        MeasurementRegistry.get_measurement(amount=20, unit="lb.", name="whole turkey"),
    )
    instructions: tuple[str, ...] = (
        "Two days before roasting, bring water and salt to boil in large pot.",
        "When clear, remove from heat and add sugar.",
        "Refridgerate overnight.",
        "Rinse turkey and then place in a bag. Add the brine.",
        "Refridgerate together for 8-12 hours overnight.",
        "Wash turkey. Spatchcock.",
        "Roast for 4.25 - 4.75 hours at 325 F.",
        "Bird is fully cooked when thickest part is 180 F.",
        "Remove foil for last 30 minutes to allow crisping.",
    )


default_recipe_registry.add_recipe(recipe=RoastTurkey())
