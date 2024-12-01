from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class ApplePieFilling(Recipe):
    name: str = "Apple Pie Filling"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1, unit="Pie", name="crust"),
        MeasurementRegistry.get_measurement(amount=3, unit="lbs.", name="(about 5) Granny Smith apples"),
        MeasurementRegistry.get_measurement(amount=2, unit="tbsp.", name="butter"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="cup", name="sugar"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="cup", name="brown sugar"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="lemon juice"),
        MeasurementRegistry.get_measurement(amount=2, unit="tsp.", name="cinnamon"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="nutmeg"),
        MeasurementRegistry.get_measurement(amount=2, unit="tbsp.", name="flour"),
        MeasurementRegistry.get_measurement(amount=2, unit="tbsp.", name="raw sugar"),
    )
    instructions: tuple[str, ...] = (
        "Peel and core apples; slice thinly. Toss apples with all dry ingredients except raw sugar. Cover and refrigerate for at least 4 hours.",
        "Drain and reserve liquid in a small saucepan; bring liquid to simmer and reduce by half (stir constantly).",
        "Pour over apples and toss to combine. Pour into pie crust and seal. Sprinkle with raw sugar.",
        "Bake to pie crust instructions.",
    )


default_recipe_registry.add_recipe(recipe=ApplePieFilling())
