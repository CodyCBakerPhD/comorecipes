from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class GreenBeanCasserole(Recipe):
    name: str = "Green Bean Casserole"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=2.0, unit="cans", name="French-style green beans"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="can", name="cream of mushroom soup"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="can", name="French-fried onions"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="milk"),
        MeasurementRegistry.get_measurement(amount=0.125, unit="tsp", name="pepper"),
    ]
    instructions: list[str] = [
        "Drain green beans. Mix soup, milk, pepper in a bowl. Add beans and mix together. Add half of the onions, give a quick stir.",
        "Place in casserole dish and bake for 25 minutes at 350° F. Add remaining onions to top and bake another 5 minutes, keeping close watch for burning.",
    ]


default_recipe_registry.add_recipe(recipe=GreenBeanCasserole())
