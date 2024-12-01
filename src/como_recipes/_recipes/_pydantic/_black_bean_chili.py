from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class BlackBeanChili(Recipe):
    name: str = "Black Bean Chili"
    tags: tuple[str, ...] = "American"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=4, unit="cloves", name="garlic"),
        MeasurementRegistry.get_measurement(amount=1 / 3, unit="white", name="onion, minced"),
        MeasurementRegistry.get_measurement(amount=1, unit="qt", name="jar of canned garden tomatoes"),
        MeasurementRegistry.get_measurement(amount=4, unit="tbsp", name="chili powder"),
        MeasurementRegistry.get_measurement(amount=2, unit="tsp", name="cumin"),
        MeasurementRegistry.get_measurement(amount=2, unit="tsp", name="oregano"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp", name="salt"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tsp", name="cayenne pepper"),
        MeasurementRegistry.get_measurement(amount=1, unit="can", name="black beans"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp", name="peanut oil"),
    )
    instructions: tuple[str, ...] = (
        "Carefully caramelize onions and garlic. Add tomatoes. Mix all dry ingredients separately and add to mixture. Add beans and oil. Stir and simmer for at least 15 minutes.",
    )


default_recipe_registry.add_recipe(recipe=BlackBeanChili())
