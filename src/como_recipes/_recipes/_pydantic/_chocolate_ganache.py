from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class ChocolateGanache(Recipe):
    name: str = "Chocolate Ganache"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=2, unit="cups", name="semi-sweet chocolate"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="heavy cream"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="vanilla extract"),
    )
    instructions: tuple[str, ...] = (
        "Combine chocolate and heavy cream in a small saucepan over medium heat.",
        "Stir frequently until chocolate is melted and mixture is smooth.",
        "Remove from heat, stir in vanilla extract.",
        "Allow chocolate to cool slightly, about 5 minutes.",
    )


default_recipe_registry.add_recipe(recipe=ChocolateGanache())
