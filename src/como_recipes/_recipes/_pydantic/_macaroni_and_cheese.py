from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class MacaroniAndCheese(Recipe):
    name: str = "Macaroni and Cheese"
    tags: tuple[str, ...] = "American"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=8, unit="oz.", name="elbow pasta"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="cup", name="butter"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="cup", name="flour"),
        MeasurementRegistry.get_measurement(
            amount=2,
            unit="cups",
            name="of any combination between 2% milk (for thin consistency) and heavy cream (very thick texture)",
        ),
        MeasurementRegistry.get_measurement(amount=7, unit="oz.", name="English aged cheddar"),
        MeasurementRegistry.get_measurement(amount=3 / 4, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="pepper"),
        MeasurementRegistry.get_measurement(amount=1 / 8, unit="tsp.", name="paprika"),
    )
    instructions: tuple[str, ...] = (
        "Cook pasta ahead of time. Cut 75% of cheese into small cubes or shred. Shred remaining 25%.",
        "Melt butter and slowly whisk in flour. Do not cook too much.",
        "Slowly whisk in milk or cream. When mixture is warm, thoroughly melt 75% of cheese.",
        "Season.",
        "Mix pasta into mixture. Layer into dish, sprinkling remaining 25% of cheese across layers, leaving some for the top.",
        "Bake for 15 minutes at 325 F; optionally, broil the top for added flavor and texture.",
    )


default_recipe_registry.add_recipe(recipe=MacaroniAndCheese())
