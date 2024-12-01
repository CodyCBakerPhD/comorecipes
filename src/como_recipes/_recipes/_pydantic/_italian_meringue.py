from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class ItalianMeringue(Recipe):
    name: str = "Italian Meringue"
    tags: tuple[str, ...] = ("Italian",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1, unit="cup", name="sugar"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="water"),
        MeasurementRegistry.get_measurement(amount=4, unit="egg", name="whites, room temperature"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="cream of tartar or lemon juice"),
    )
    instructions: tuple[str, ...] = (
        "Combine sugar and water in a small saucepan over high heat, brushing down sides of pot as necessary with a pastry brush dipped in water.",
        "Cook until syrup is 270 F.",
        "Combine egg whites and cream of tartar (or lemon juice) in a stand mixer with a whisk attachment.",
        "Whisk at medium speed until soft peaks form (about 2 minutes).",
        "With the mixture running, slowly drizzle in the hot syrup.",
        "Increase mixer speed to high and whisk until stiff peaks are formed.",
    )


default_recipe_registry.add_recipe(recipe=ItalianMeringue())
