from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class Falafel(Recipe):
    name: str = "Falafel"
    tags: tuple[str, ...] = ("Greek",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1, unit="lb.", name="dry chickpeas"),
        MeasurementRegistry.get_measurement(amount=1, unit="small", name="white onion"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="cup", name="parsley"),
        MeasurementRegistry.get_measurement(amount=5, unit="gloves", name="garlic"),
        MeasurementRegistry.get_measurement(amount=3 / 2, unit="tbsp.", name="flour"),
        MeasurementRegistry.get_measurement(amount=7 / 4, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=2, unit="tsp.", name="cumin"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="coriander"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="pepper"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="cayenne"),
        MeasurementRegistry.get_measurement(amount=1 / 8, unit="tsp.", name="cardamom"),
    )
    instructions: tuple[str, ...] = (
        "Soak beans overnight.",
        "Grind entire mixture well in a food processor.",
        "Shape and deep fry at 375 F until golden brown.",
    )


default_recipe_registry.add_recipe(recipe=Falafel())
