from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class SweetFireRub(Recipe):
    name: str = "Sweet Fire Rub"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="brown sugar"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="white sugar"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="cup", name="paprika"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="onion powder"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="garlic powder"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="chili powder"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="cayenne pepper"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tbsp.", name="salt & pepper"),
    )
    instructions: tuple[str, ...] = ("Mix together and store in pantry.",)


default_recipe_registry.add_recipe(recipe=SweetFireRub())
