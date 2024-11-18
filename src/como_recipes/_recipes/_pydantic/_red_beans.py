from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class RedBeans(Recipe):
    name: str = "Red Beans"
    measurements: tuple[Measurement] = (
        MeasurementRegistry.get_measurement(amount=1.0, unit="recipes", name="worth of rice"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="olive oil"),
        MeasurementRegistry.get_measurement(amount=4.0, unit="cloves", name="garlic"),
        MeasurementRegistry.get_measurement(amount=0.3333333333333333, unit="white", name="onion"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="stalk", name="celery"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="bay", name="leaves"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="cayenne pepper"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="thyme"),
        MeasurementRegistry.get_measurement(amount=0.125, unit="tsp.", name="sage"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="parsley"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="Cajun seasoning"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="water"),
    )
    instructions: tuple[str] = (
        "Make rice. Mix spices together.",
        "Carefully caramelize garlic, onion, and celery in oil.",
        "Add water to onions and garlic, then mix in spices.",
        "Add beans and any other add-ins, simmer for at least 15 minutes.",
        "Serve on rice.",
    )


default_recipe_registry.add_recipe(recipe=RedBeans())
