from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class TamariSauce(Recipe):
    name: str = "Tamari Sauce"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="sesame oil"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tbsp.", name="ginger, minced"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="cloves", name="garlic, minced"),
        MeasurementRegistry.get_measurement(amount=1.5, unit="tbsp.", name="tamari"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="rice vinegar"),
        MeasurementRegistry.get_measurement(amount=0.75, unit="tbsp.", name="maple syrup"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="water"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tbsp.", name="cornstarch"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="pepper"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="red pepper flakes"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="paprika"),
    )
    instructions: tuple[str, ...] = (
        "Mix water and cornstarch to make a slurry.",
        "Heat oil in saucepan. Add everything except cornstarch mixture, cook for 2 minutes.",
        "Add cornstarch mixture to thicken.",
        "Season with spices, cook until desired consistency.",
    )


default_recipe_registry.add_recipe(recipe=TamariSauce())
