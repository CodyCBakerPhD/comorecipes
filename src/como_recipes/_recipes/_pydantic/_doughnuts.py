from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class Doughnuts(Recipe):
    name: str = "Doughnuts"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1 / 8, unit="o.z", name="activate dry yeast"),
        MeasurementRegistry.get_measurement(amount=1 / 8, unit="cup", name="warm water"),
        MeasurementRegistry.get_measurement(amount=3 / 4, unit="cup", name="lukewarm milk"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="cup", name="sugar"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=1, unit="large", name="egg"),
        MeasurementRegistry.get_measurement(amount=1 / 6, unit="cup", name="shortening"),
        MeasurementRegistry.get_measurement(amount=5 / 2, unit="cups", name="all-purpose flour"),
        MeasurementRegistry.get_measurement(amount=1, unit="qt.", name="vegetable oil"),
        MeasurementRegistry.get_measurement(amount=1 / 6, unit="cup", name="butter"),
        MeasurementRegistry.get_measurement(amount=1, unit="cups", name="powdered sugar"),
        MeasurementRegistry.get_measurement(amount=3 / 4, unit="tsp.", name="vanilla"),
        MeasurementRegistry.get_measurement(amount=2, unit="tbsp.", name="hot water"),
    )
    instructions: tuple[str, ...] = (
        "Activate yeast.",
        "In large bowl, mix together activated yeast, milk, sugar, salt, eggs, shortening, and 1 cup of the flour.",
        "Mix for a few minutes at low speed.",
        "Beat in remaining flour 1/2 cup at a time, until dough no longer sticks to the bowl.",
        "Knead by hand for 5 minutes until smooth and elastic.",
        "Prove until doubled, about an hour.",
        "Gently roll out to 1/2 inch thickness. Shape as desired.",
        "Cover with cloth and prove again until doubled, about 40 minutes.",
        "Heat oil to 350 F.",
        "Slide doughnuts into hot oil using a wide spatula.",
        "Turn over as they rise to the surface. Fry each side until golden brown.",
        "Drain and cool on wire rack.",
        "Melt the butter in a saucepan, incorporate sifted powdered sugar and vanilla.",
        "Dip doughnuts in glaze while still warm.",
    )


default_recipe_registry.add_recipe(recipe=Doughnuts())
