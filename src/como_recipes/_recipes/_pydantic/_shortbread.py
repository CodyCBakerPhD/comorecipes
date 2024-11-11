from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class Shortbread(Recipe):
    name: str = "Shortbread"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="butter, room temperature"),
        MeasurementRegistry.get_measurement(amount=0.3333333333333333, unit="cup", name="sugar"),
        MeasurementRegistry.get_measurement(amount=0.3333333333333333, unit="cup", name="brown sugar"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="large", name="egg yolk"),
        MeasurementRegistry.get_measurement(amount=0.75, unit="tsp.", name="vanilla extract"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=2.25, unit="cups", name="flour"),
    ]
    instructions: list[str] = [
        "Preheat oven to 350 °F. Line a 13x9 baking pan with parchment paper.",
        "Using a stand mixer, beat butter until well creamed.",
        "Add sugars and beat until light and fluffy.",
        "Add egg yolk and vanilla extract. Combine well, scraping the sides.",
        "Add flour gradually, scraping the sides.",
        "Halfway through incorporating flour, sprinkle in salt.",
        "Do not overwork the dough.",
        "Drop dough over baking pan and evenly press onto bottom.",
        "Bake for about 23 minutes or until lightly golden brown.",
    ]


default_recipe_registry.add_recipe(recipe=Shortbread())
