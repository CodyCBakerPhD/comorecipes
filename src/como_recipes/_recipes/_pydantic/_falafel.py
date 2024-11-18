from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class Falafel(Recipe):
    name: str = "Falafel"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1.0, unit="lb.", name="dry chickpeas"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="small", name="white onion"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="cup", name="parsley"),
        MeasurementRegistry.get_measurement(amount=5.0, unit="gloves", name="garlic"),
        MeasurementRegistry.get_measurement(amount=1.5, unit="tbsp.", name="flour"),
        MeasurementRegistry.get_measurement(amount=1.75, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tsp.", name="cumin"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="coriander"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="pepper"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="cayenne"),
        MeasurementRegistry.get_measurement(amount=0.125, unit="tsp.", name="cardamom"),
    )
    instructions: tuple[str, ...] = (
        "Soak beans overnight.",
        "Grind entire mixture well in a food processor.",
        "Shape and deep fry at 375 °F until golden brown.",
    )


default_recipe_registry.add_recipe(recipe=Falafel())
