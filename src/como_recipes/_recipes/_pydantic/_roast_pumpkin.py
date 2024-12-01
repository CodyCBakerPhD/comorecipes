from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class RoastPumpkin(Recipe):
    name: str = "Roast Pumpkin"
    tags: tuple[str, ...] = "American"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=5 / 2, unit="lb", name="sugar pumpkin"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="coconut oil"),
    )
    instructions: tuple[str, ...] = (
        "Cut pumpkin in half length-wise. Scrape out seeds and string.",
        "Brush with oil and pierce outer skin a few times for steam to escape. Bake for 45-50 minutes at 350 F. Let cool and then scoop out meat.",
    )


default_recipe_registry.add_recipe(recipe=RoastPumpkin())
