from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class PotatoesAuGratin(Recipe):
    name: str = "Potatoes Au Gratin"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=4.0, unit="russet", name="potatoes"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="onion", name=""),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="salt and pepper"),
        MeasurementRegistry.get_measurement(amount=3.0, unit="tbsp.", name="butter"),
        MeasurementRegistry.get_measurement(amount=3.0, unit="tbsp.", name="flour"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="cups", name="whole milk"),
        MeasurementRegistry.get_measurement(amount=1.5, unit="cup", name="cheddar"),
    ]
    instructions: list[str] = [
        "Preheat to 400 °F. Butter the casserole dish.",
        "Layer 1/2 of potatoes into bottom of dish. Top with onions and add remaining potatoes. Season with salt and pepper.",
        "In medium-sized pan, melt butter over medium heat. Mix in flour and salt. Stir constantly with whisk for 1 minute. Stir in milk.",
        "Cook until thickened, then stir in cheese all at once.",
        "Continue stirring until melted, about 30 to 60 seconds. Pour cheese over potatoes and cover with dish with aluminum foil. Bake 90 minutes.",
    ]


default_recipe_registry.add_recipe(recipe=PotatoesAuGratin())
