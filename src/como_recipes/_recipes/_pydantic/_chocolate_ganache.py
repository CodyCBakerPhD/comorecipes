from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class ChocolateGanache(Recipe):
    name: str = "Chocolate Ganache"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=2.0, unit="cups", name="semi-sweet chocolate"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="heavy cream"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="vanilla extract"),
    ]
    instructions: list[str] = [
        "Combine chocolate and heavy cream in a small saucepan over medium heat.",
        "Stir frequently until chocolate is melted and mixture is smooth.",
        "Remove from heat, stir in vanilla extract.",
        "Allow chocolate to cool slightly, about 5 minutes.",
    ]


default_recipe_registry.add_recipe(recipe=ChocolateGanache())
