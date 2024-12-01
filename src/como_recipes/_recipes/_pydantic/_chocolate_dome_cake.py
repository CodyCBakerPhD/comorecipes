from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class ChocolateDomeCake(Recipe):
    name: str = "Chocolate Dome Cake"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=4, unit="large", name="eggs"),
        MeasurementRegistry.get_measurement(amount=1, unit="cup", name="sugar"),
        MeasurementRegistry.get_measurement(amount=3 / 4, unit="cup", name="cake flour"),
        MeasurementRegistry.get_measurement(amount=1, unit="cup", name="whipping cream"),
        MeasurementRegistry.get_measurement(amount=5, unit="oz.", name="semi-sweet chocolate"),
        MeasurementRegistry.get_measurement(amount=7, unit="oz.", name="high-quality chocolate for coating"),
        MeasurementRegistry.get_measurement(amount=1, unit="1/2", name="cup raspberries"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="sugar"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="lime juice"),
    )
    instructions: tuple[str, ...] = (
        "Preheat to 350 F. Whip eggs and sugar until thick and frothy. Fold in flour. Bake in round bowl for 1 hour.",
        "Whip cream, fold in melted chocolate.",
        "Slice cake into three layers and fill evenly with mousse. Lay saran wrap large and flat enough to cover the surface of the cake.",
        "Melt milk chocolate and delicately spread on saran wrap. Carefully move into the bowl used to bake the cake, and gently place cake back in the bowl.",
        "Refrigerate until chocolate has bound and solidified.",
        "Blend sauce ingredients, keep cold until served.",
    )


default_recipe_registry.add_recipe(recipe=ChocolateDomeCake())
