from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class TamariSauce(Recipe):
    name: str = "Tamari Sauce"
    tags: tuple[str, ...] = "Asian"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="sesame oil"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tbsp.", name="ginger, minced"),
        MeasurementRegistry.get_measurement(amount=2, unit="cloves", name="garlic, minced"),
        MeasurementRegistry.get_measurement(amount=3 / 2, unit="tbsp.", name="tamari"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="rice vinegar"),
        MeasurementRegistry.get_measurement(amount=3 / 4, unit="tbsp.", name="maple syrup"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="water"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tbsp.", name="cornstarch"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="pepper"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="red pepper flakes"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="paprika"),
    )
    instructions: tuple[str, ...] = (
        "Mix water and cornstarch to make a slurry.",
        "Heat oil in saucepan. Add everything except cornstarch mixture, cook for 2 minutes.",
        "Add cornstarch mixture to thicken.",
        "Season with spices, cook until desired consistency.",
    )


default_recipe_registry.add_recipe(recipe=TamariSauce())
