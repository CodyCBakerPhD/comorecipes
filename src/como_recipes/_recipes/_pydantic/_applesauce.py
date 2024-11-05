from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._registration import default_recipe_registry, MeasurementRegistry


class Applesauce(Recipe):
    name: str = "Applesauce"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=4.0, unit="", ingredient="apples"),
        MeasurementRegistry.get_measurement(amount=0.75, unit="cup", name="water"),
        MeasurementRegistry.get_measurement(amount=0.0625, unit="cup", name="white sugar"),
        MeasurementRegistry.get_measurement(amount=0.0625, unit="cup", name="brown sugar"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="ground cinnamon"),
    ]
    instructions: list[str] = [
        "Peel and core apples.",
        "Combine everything and cook over medium heat for 15-20 minutes (until apples are soft).",
        "Allow to cool, then mash with fork or potato masher.",
    ]


default_recipe_registry.add_recipe(recipe=Applesauce())
