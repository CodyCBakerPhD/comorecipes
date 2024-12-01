from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class HappyPlums(Recipe):
    name: str = "Happy Plums"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=4, unit="plums", name=""),
        MeasurementRegistry.get_measurement(amount=2, unit="tbsp.", name="sugar"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="coconut oil"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="cup", name="basalmic vinegar"),
        MeasurementRegistry.get_measurement(amount=1 / 8, unit="tsp.", name="vanilla extract"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="chopped fresh rosemary"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="honey"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="sour cream"),
    )
    instructions: tuple[str, ...] = (
        "Preheat oven to 350 F. Cut plums in half and remove the pits. Coat baking pan with oil. Brush plums with oil, then sprinkle a thin layer of sugar on each. Bake for 20 minutes.",
        "In a pot, combine basalmic vinegar and rosemary (Note: basalmic syrup is very stinky, ventilate well). Bring the mixture to a boil and lower to a simmer, reducing for about 8 minutes.",
        "Add honey and vanilla, stir until dissolved. Remove mixture from heat and strain the basalmic syrup to separate from the rosemary.",
    )


default_recipe_registry.add_recipe(recipe=HappyPlums())
