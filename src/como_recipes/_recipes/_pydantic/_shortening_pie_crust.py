from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class ShorteningPieCrust(Recipe):
    name: str = "Shortening Pie Crust"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=2.0, unit="tsp.", name="sugar"),
        MeasurementRegistry.get_measurement(amount=2.25, unit="cup", name="flour"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="cold shortening"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="ice water"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="egg", name="yolk with a little water"),
    )
    instructions: tuple[str, ...] = (
        (
            "Pulse flour, sugar and salt in food processor to combine. "
            "Add cold shortening and pulse until pea-size pieces remain."
        ),
        (
            "Transfer to bowl and cover, refrigerate for at least 30 minutes. "
            "Drizzle ice water over mixture and mix thoroughly with hands."
        ),
        "Divide in half, press into discs and store back in the refrigerator for at least 1 hour.",
        (
            "Preheat to 350 °F. Move discs into pie tin. Shape and add filling, then top. "
            "Seal joint and add air-holes in the top. Brush top with egg yolk and water mixture, not overdoing it."
        ),
        "Bake for 90 to 100 minutes for fruit pies.",
    )


default_recipe_registry.add_recipe(recipe=ShorteningPieCrust())
