from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class SlowCookedRibs(Recipe):
    name: str = "Slow-Cooked Ribs"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(
            amount=0.3333333333333333, unit="cup", name="premade Sweet Fire Rub (see recipe)"
        ),
        MeasurementRegistry.get_measurement(amount=0.5, unit="rack", name="baby back ribs"),
    ]
    instructions: list[str] = [
        (
            "Thoroughly rub dry mix onto ribs in a separate bowl. "
            "Drizzle small amount of water into bottom of pan and cover with foil."
        ),
        "Choose a BBQ sauce.",
        "Bake in oven for 3 hours at 280°F. Finish by grilling briefly at high heat to seal in BBQ sauce.",
    ]


default_recipe_registry.add_recipe(recipe=SlowCookedRibs())
