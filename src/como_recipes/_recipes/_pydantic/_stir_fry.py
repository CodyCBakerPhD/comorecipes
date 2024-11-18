from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class StirFry(Recipe):
    name: str = "Stir Fry"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1.0, unit="serving", name="rice"),
        MeasurementRegistry.get_measurement(amount=3.0, unit="tbsp", name="peanut oil"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="serving", name="beef, chicken, pork, or shrimp"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="serving", name="tofu"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="serving", name="shallots"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="serving", name="garlic"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="serving", name="carrots"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="serving", name="broccoli"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="serving", name="cauliflower"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="serving", name="cabbage"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="serving", name="green beans"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="serving", name="pea pods"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="serving", name="spinach"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="serving", name="water chestnut"),
    )
    instructions: tuple[str, ...] = (
        "Meat: cut into thin strips and fry in separate pan without onions/garlic",
        "Tofu: get extra-firm and deep fry covered in cornstarch",
        (
            "In main woc, fry vegetables in order of cooking time (roughly given in order of ingredients). "
            "Add sauce and garnish with meat or tofu."
        ),
    )


default_recipe_registry.add_recipe(recipe=StirFry())
