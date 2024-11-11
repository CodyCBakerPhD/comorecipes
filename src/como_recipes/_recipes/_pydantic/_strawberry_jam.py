from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class StrawberryJam(Recipe):
    name: str = "Strawberry Jam"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=1.5, unit="", name="cups of thinly sliced strawberries"),
        MeasurementRegistry.get_measurement(amount=40.0, unit="", name="g. sugar"),
        MeasurementRegistry.get_measurement(amount=40.0, unit="", name="g. brown sugar"),
        MeasurementRegistry.get_measurement(amount=20.0, unit="", name="g. honey"),
        MeasurementRegistry.get_measurement(amount=2.25, unit="tbsp.", name="cornstarch"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="", name="tsp. vanilla extract"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="lime juice"),
    ]
    instructions: list[str] = [
        "Carefully weigh the white and brown sugar into a small bowl.",
        "Save adding honey this mixture until just ready to add to strawberries.",
        "Heat strawberries slowly over medium-low heat stirring constantly, until juices begin leaking.",
        "Then quickly incorporate the sugars and cornstarch and stir well until everything is homogeneous.",
        "Increase heat to just above medium, and reach a boil stirring often.",
        "When mixture is at boil (it remains boiling upon stirring) then stir constantly for one minute and then remove from heat.",
        "Let cool before using.",
    ]


default_recipe_registry.add_recipe(recipe=StrawberryJam())
