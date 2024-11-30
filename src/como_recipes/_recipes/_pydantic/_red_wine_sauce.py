from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class RedWineSauce(Recipe):
    name: str = "Red Wine Sauce"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="olive oil"),
        MeasurementRegistry.get_measurement(amount=2, unit="cloves", name="garlic"),
        MeasurementRegistry.get_measurement(amount=3 / 4, unit="cup", name="red wine"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="cup", name="water"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="soy sauce"),
        MeasurementRegistry.get_measurement(amount=3, unit="tbsp.", name="butter"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="parsley"),
    )
    instructions: tuple[str, ...] = (
        "Heat oil over medium-high heat. Cook garlic for ~30 seconds. Add wine and reach a simmer.",
        "Reduce to half, about 2-3 minutes. Add water and soy sauce. Reduce to half again.",
        "Reduce heat to medium-low and whisk in butter, 1 tbsp. at a time. Stir in parsley and serve.",
    )


default_recipe_registry.add_recipe(recipe=RedWineSauce())
