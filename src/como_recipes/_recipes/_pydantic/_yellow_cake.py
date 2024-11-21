from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class YellowCake(Recipe):
    name: str = "Yellow Cake"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="butter"),
        MeasurementRegistry.get_measurement(amount=1.5, unit="cup", name="sugar"),
        MeasurementRegistry.get_measurement(amount=8.0, unit="egg", name="yolks"),
        MeasurementRegistry.get_measurement(amount=0.75, unit="cup", name="milk"),
        MeasurementRegistry.get_measurement(amount=1.5, unit="tsp.", name="vanilla"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="cups", name="cake flour"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tsp.", name="baking powder"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="salt"),
    )
    instructions: tuple[str, ...] = (
        "Preheat to 350 F. Grease cake pan or cupcake pan.",
        "Sift together flour, baking powder, and salt.",
        "In separate bowl, cream butter and sugar until light and fluffy.",
        "Beat in egg yolks one at a time, then stir in the vanilla.",
        "Beat in the flour mixture alternately with the milk, mixing just until incorporated.",
        "Pour batter into pan. Bake for 25-30 minutes.",
        "Cool 15 minutes before turning out onto rack or plate.",
    )


default_recipe_registry.add_recipe(recipe=YellowCake())
