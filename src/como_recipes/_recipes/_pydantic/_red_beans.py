from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class RedBeans(Recipe):
    name: str = "Red Beans"
    tags: tuple[str, ...] = "American"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1, unit="recipes", name="worth of rice"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="olive oil"),
        MeasurementRegistry.get_measurement(amount=4, unit="cloves", name="garlic"),
        MeasurementRegistry.get_measurement(amount=1 / 3, unit="white", name="onion"),
        MeasurementRegistry.get_measurement(amount=1, unit="stalk", name="celery"),
        MeasurementRegistry.get_measurement(amount=2, unit="bay", name="leaves"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="cayenne pepper"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="thyme"),
        MeasurementRegistry.get_measurement(amount=1 / 8, unit="tsp.", name="sage"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="parsley"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="Cajun seasoning"),
        MeasurementRegistry.get_measurement(amount=1, unit="cup", name="water"),
    )
    instructions: tuple[str, ...] = (
        "Make rice. Mix spices together.",
        "Carefully caramelize garlic, onion, and celery in oil.",
        "Add water to onions and garlic, then mix in spices.",
        "Add beans and any other add-ins, simmer for at least 15 minutes.",
        "Serve on rice.",
    )


default_recipe_registry.add_recipe(recipe=RedBeans())
