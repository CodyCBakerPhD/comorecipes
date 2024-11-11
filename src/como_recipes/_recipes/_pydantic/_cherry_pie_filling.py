from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class CherryPieFilling(Recipe):
    name: str = "Cherry Pie Filling"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=1.0, unit="pie", name="crust"),
        MeasurementRegistry.get_measurement(amount=4.0, unit="cups", name="fresh tart cherries or"),
        MeasurementRegistry.get_measurement(amount=6.0, unit="cups", name="frozen tart cherries"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="sugar"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="cup", name="cornstarch"),
    ]
    instructions: list[str] = [
        "Place cherries into a saucepan over medium heat and cover. Heat cherries until they release their juices and simmer 10 to 15 minutes. Stir often.",
        "In a bowl, whisk sugar with cornstarch until smooth. Pour mixture into cherries and juice and combine. Return to low heat, bring to simmer, and cook until filling has thickened (about 2 minutes).",
        "Remove from heat and use as pie filling. Cook to pie crust instructions.",
    ]


default_recipe_registry.add_recipe(recipe=CherryPieFilling())
