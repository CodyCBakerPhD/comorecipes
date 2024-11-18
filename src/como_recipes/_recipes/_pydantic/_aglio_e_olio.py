from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class AglioEOlio(Recipe):
    name: str = "Aglio E Olio"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=2.0, unit="qt.", name="water"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="lb.", name="thin spaghetti"),
        MeasurementRegistry.get_measurement(amount=0.3333333333333333, unit="cup", name="olive oil"),
        MeasurementRegistry.get_measurement(amount=8.0, unit="large", name="cloves of garlic"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tsp.", name="crushed red pepper"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="cup", name="parsley"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="fresh Parmesan"),
    )
    instructions: tuple[str, ...] = (
        "Bring water and salt to boil. Cook pasta. Set aside 3/2 cup of pasta water before draining.",
        "Heat olive oil over medium heat in a large pot.",
        "Add garlic and cook for 1-2 minutes, stirring frequently until it just turns golden.",
        "Add red pepper and cook 30 seconds more.",
        "Carefully add reserved pasta water and bring to boil.",
        "Lower heat and simmer for 5 minutes, until liquid is reduced by about a third.",
        "Incorporate pasta, parsley, and Permesan.",
    )


default_recipe_registry.add_recipe(recipe=AglioEOlio())
