from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class FriedRice(Recipe):
    name: str = "Fried Rice"
    tags: tuple[str, ...] = ("Asian",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1, unit="serving", name="of chilled rice"),
        MeasurementRegistry.get_measurement(amount=1, unit="serving", name="fried tofu"),
        MeasurementRegistry.get_measurement(amount=2, unit="eggs", name=""),
        MeasurementRegistry.get_measurement(amount=3, unit="tbsp.", name="butter"),
        MeasurementRegistry.get_measurement(amount=3, unit="cloves", name="garlic"),
        MeasurementRegistry.get_measurement(amount=1, unit="small", name="white onion"),
        MeasurementRegistry.get_measurement(amount=1, unit="large", name="carrot"),
        MeasurementRegistry.get_measurement(amount=1, unit="package", name="Shitake mushrooms"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="frozen or fresh peas"),
        MeasurementRegistry.get_measurement(amount=4, unit="tbsp.", name="soy sauce"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="sesame oil"),
    )
    instructions: tuple[str, ...] = (
        "Make and chill rice a day ahead of time.",
        "Fry tofu at same time.",
        "Scramble eggs and set aside.",
        "Stiry fry onion and garlic.",
        "Add other vegetables until cooked.",
        "Add rice and seasonings, fry until ready.",
    )


default_recipe_registry.add_recipe(recipe=FriedRice())
