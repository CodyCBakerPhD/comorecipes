from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class PumpkinCreamCoffeeSauce(Recipe):
    name: str = "Pumpkin Cream Coffee Sauce"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="heavy whipping cream"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="granulated sugar"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="pumpkin puree"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="pumpkin pie spice"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="vanilla extract"),
    ]
    instructions: list[str] = [
        "Combine heavy cream, sugar, pumpkin puree and pumpkin spice in a saucepan. Whisk over medium heat until sugar is dissolved and cream mixture begins to steam.",
        "DO NOT BOIL. Remove from heat and whisk in vanilla extract. Strain through a fine mesh strainer or cheesecloth, transfer to mason jar or pitcher.",
        "Refrigerate until cool.",
    ]


default_recipe_registry.add_recipe(recipe=PumpkinCreamCoffeeSauce())
