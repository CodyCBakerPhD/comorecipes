from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class GreenBeanCasserole(Recipe):
    name: str = "Green Bean Casserole"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=2, unit="cans", name="French-style green beans"),
        MeasurementRegistry.get_measurement(amount=1, unit="can", name="cream of mushroom soup"),
        MeasurementRegistry.get_measurement(amount=1, unit="can", name="French-fried onions"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="milk"),
        MeasurementRegistry.get_measurement(amount=1 / 8, unit="tsp", name="pepper"),
    )
    instructions: tuple[str, ...] = (
        "Drain green beans. Mix soup, milk, pepper in a bowl. Add beans and mix together. Add half of the onions, give a quick stir.",
        "Place in casserole dish and bake for 25 minutes at 350 F. Add remaining onions to top and bake another 5 minutes, keeping close watch for burning.",
    )


default_recipe_registry.add_recipe(recipe=GreenBeanCasserole())
