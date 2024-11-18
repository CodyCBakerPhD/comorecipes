from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class CollardGreens(Recipe):
    name: str = "Collard Greens"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=3.0, unit="tbsp.", name="olive oil"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="onion", name=""),
        MeasurementRegistry.get_measurement(amount=2.0, unit="cloves", name="garlic"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="pepper"),
        MeasurementRegistry.get_measurement(amount=3.0, unit="cups", name="chicken flavored vegetable broth"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="pinch", name="red pepper flakes"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="lb.", name="fresh collard greens"),
    )
    instructions: tuple[str, ...] = (
        "Heat oil in very large pot over medium heat.",
        "Add onion, cook until tender. Add garlic. Add collard greens, fry until they wilt.",
        "Pour in broth, season with spices. Reduce heat to low, cover, and simmer for 45 minutes or until tender.",
    )


default_recipe_registry.add_recipe(recipe=CollardGreens())
