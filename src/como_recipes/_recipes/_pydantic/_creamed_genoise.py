from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class CreamedGenoise(Recipe):
    name: str = "Creamed Genoise"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=375 / 2, unit="g.", name="butter, room temperature"),
        MeasurementRegistry.get_measurement(amount=375 / 2, unit="g.", name="sugar"),
        MeasurementRegistry.get_measurement(amount=3, unit="", name="beaten eggs, room temperature"),
        MeasurementRegistry.get_measurement(amount=375 / 2, unit="g.", name="cake flour"),
        MeasurementRegistry.get_measurement(amount=1, unit="", name="tsp. baking powder"),
        MeasurementRegistry.get_measurement(amount=25, unit="ml.", name="milk"),
        MeasurementRegistry.get_measurement(amount=1, unit="", name="tsp. vanilla extract"),
    )
    instructions: tuple[str, ...] = (
        "Preheat to 350 F.",
        "Cream butter and sugar with wooden spoon, then set in stand mixer on medium-high for about two minutes, constantly scraping the sides.",
        "Then begin adding very small drizzle of the egg into the butter mixture while it remains in the stand mixer on medium-high. Continue until all egg is incorporated.",
        "Now remove from stand mixer and over the course of several gentle folds, sift and incorporate the flour and baking powder.",
        "Halfway through the folding, add half the milk/vanilla mixture. Add remaining at the end.",
        "Bake for around 20 minutes.",
    )


default_recipe_registry.add_recipe(recipe=CreamedGenoise())
