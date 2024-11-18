from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class BrownieIcing(Recipe):
    name: str = "Brownie Icing"
    measurements: tuple[Measurement] = (
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="sifted Dutch cocoa"),
        MeasurementRegistry.get_measurement(amount=1.5, unit="tbsp.", name="butter"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="cups", name="sifted powdered sugar"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="evaporated milk"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="vanilla"),
    )
    instructions: tuple[str] = (
        "Do not forget to sift dry ingredients.",
        "Melt butter in saucepan. Add sifted cocoa and remove pan from heat.",
        "Stir in sifted powdered sugar and other ingredients, saving vanilla for last to keep it smooth.",
        "Add more powdered sugar as necessary for consistency.",
    )


default_recipe_registry.add_recipe(recipe=BrownieIcing())
