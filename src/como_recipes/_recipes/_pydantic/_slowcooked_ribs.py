from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class SlowCookedRibs(Recipe):
    name: str = "Slow-Cooked Ribs"
    tags: tuple[str, ...] = "American"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1 / 3, unit="cup", name="premade Sweet Fire Rub (see recipe)"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="rack", name="baby back ribs"),
    )
    instructions: tuple[str, ...] = (
        "Thoroughly rub dry mix onto ribs in a separate bowl. Drizzle small amount of water into bottom of pan and cover with foil.",
        "Choose a BBQ sauce.",
        "Bake in oven for 3 hours at 280F. Finish by grilling briefly at high heat to seal in BBQ sauce.",
    )


default_recipe_registry.add_recipe(recipe=SlowCookedRibs())
