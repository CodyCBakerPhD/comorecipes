from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class MirrorGlaze(Recipe):
    name: str = "Mirror Glaze"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=20.0, unit="g", name="Agar Agar"),
        MeasurementRegistry.get_measurement(amount=170.0, unit="mL", name="water"),
        MeasurementRegistry.get_measurement(amount=300.0, unit="mL", name="corn syrup"),
        MeasurementRegistry.get_measurement(amount=150.0, unit="g", name="sugar"),
        MeasurementRegistry.get_measurement(amount=200.0, unit="g", name="condensed milk"),
        MeasurementRegistry.get_measurement(amount=300.0, unit="g", name="white chocolate"),
    )
    instructions: tuple[str, ...] = (
        "Divide water in two.",
        "Place Agar Agar in one of the two halves and let sit for 4 minutes.",
        "In a large saucepan - add corn syrup, condensed milk, and remaining water over low to medium heat.",
        "Bring to slow boil, ensuring sugar has dissolved.",
        "Take saucepan off heat, let rest 1 minute before adding white chocolate to mixture.",
        "Add Agar Agar and let mixture melt.",
        "Stir and allow glaze to come to room temperature.",
    )


default_recipe_registry.add_recipe(recipe=MirrorGlaze())
