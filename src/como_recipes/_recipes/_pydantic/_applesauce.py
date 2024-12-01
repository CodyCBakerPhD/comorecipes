from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class Applesauce(Recipe):
    name: str = "Applesauce"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=4, unit="large", name="apples"),
        MeasurementRegistry.get_measurement(amount=3 / 4, unit="cup", name="water"),
        MeasurementRegistry.get_measurement(amount=1 / 16, unit="cup", name="white sugar"),
        MeasurementRegistry.get_measurement(amount=1 / 16, unit="cup", name="brown sugar"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="ground cinnamon"),
    )
    instructions: tuple[str, ...] = (
        "Peel and core apples.",
        "Combine everything and cook over medium heat for 15-20 minutes (until apples are soft).",
        "Allow to cool, then mash with fork or potato masher.",
    )


default_recipe_registry.add_recipe(recipe=Applesauce())
