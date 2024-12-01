from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class SpanishRice(Recipe):
    name: str = "Spanish Rice"
    tags: tuple[str, ...] = ("Mexican",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="butter"),
        MeasurementRegistry.get_measurement(amount=1, unit="shallot", name=""),
        MeasurementRegistry.get_measurement(amount=2, unit="cloves", name="garlic"),
        MeasurementRegistry.get_measurement(amount=1, unit="cup", name="long grain brown rice"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="salt and pepper"),
        MeasurementRegistry.get_measurement(amount=5 / 2, unit="cups", name="not-chicken broth"),
        MeasurementRegistry.get_measurement(amount=2, unit="sprigs", name="of thyme"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="parsley"),
    )
    instructions: tuple[str, ...] = (
        "Melt butter over medium heat. Add shallot and garlic, saute until tender.",
        "Add rice and stir until glossy. Add stock and herbs, bring to boil.",
        "Reduce to low or simmer and let cook for 30-40 minutes until all liquid is gone.",
        "Note: Rinse the rice beforehand to make fluffier",
    )


default_recipe_registry.add_recipe(recipe=SpanishRice())
