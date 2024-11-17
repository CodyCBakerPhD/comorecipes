from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class SauteedMushrooms(Recipe):
    name: str = "Sauteed Mushrooms"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=3.0, unit="tbsp.", name="olive oil"),
        MeasurementRegistry.get_measurement(amount=3.0, unit="tbsp.", name="butter"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="lb.", name="button mushrooms"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="clove", name="garlic"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="red wine"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="garlic salt"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="pepper"),
    ]
    instructions: list[str] = [
        "Heat oil and butter in large saucepan over medium heat.",
        "Cook all ingredients until mushrooms are lightly browned.",
        "Reduce heat to low and simmer until mushrooms are tender, about 5-8 more minutes.",
    ]


default_recipe_registry.add_recipe(recipe=SauteedMushrooms())
