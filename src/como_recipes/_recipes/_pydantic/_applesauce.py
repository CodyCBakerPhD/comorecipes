from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._registration import default_recipe_registry


class Applesauce(Recipe):
    name: str = "Applesauce"
    ingredients: list[Measurement] = [
        Measurement(name="", amount=4.0, unit="apples"),
        Measurement(name="water", amount=0.75, unit="cup"),
        Measurement(name="white sugar", amount=0.0625, unit="cup"),
        Measurement(name="brown sugar", amount=0.0625, unit="cup"),
        Measurement(name="ground cinnamon", amount=0.5, unit="tsp."),
    ]
    instructions: list[str] = [
        "Peel and core apples.",
        "Combine everything and cook over medium heat for 15-20 minutes (until apples are soft).",
        "Allow to cool, then mash with fork or potato masher.",
    ]


default_recipe_registry.update_registry(recipe=Applesauce())
