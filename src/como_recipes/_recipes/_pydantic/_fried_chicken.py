from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class FriedChicken(Recipe):
    name: str = "Fried Chicken"
    measurements: tuple[Measurement] = (
        MeasurementRegistry.get_measurement(amount=0.25, unit="serving", name="of Frying Breading"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="large", name="chicken breasts"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="cups", name="buttermilk"),
    )
    instructions: tuple[str] = (
        "Heat oil to 325 °F. Add some lime juice if feeling fruity.",
        "Cut each chicken breast in half and soak in buttermilk for a few minutes.",
        "Dredge with breading in a plastic bag for maximum cleanliness and adherence.",
        "Fry for ~13 minutes until golden brown, crispy, and thickest part of meat is 180 °F.",
    )


default_recipe_registry.add_recipe(recipe=FriedChicken())
