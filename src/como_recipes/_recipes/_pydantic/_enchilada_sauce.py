from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class EnchiladaSauce(Recipe):
    name: str = "Enchilada Sauce"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="cup", name="vegetable oil"),
        MeasurementRegistry.get_measurement(amount=1 / 8, unit="cup", name="flour"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="cup", name="dark chili powder"),
        MeasurementRegistry.get_measurement(amount=8, unit="oz.", name="can tomato sauce"),
        MeasurementRegistry.get_measurement(amount=3 / 2, unit="cups", name="water"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="cumin"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="garlic powder"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="onion powder"),
        MeasurementRegistry.get_measurement(amount=1 / 8, unit="tsp.", name="salt"),
    )
    instructions: tuple[str, ...] = (
        "Heat oil over medium-high heat. Stir in flour and chili powder.",
        "Reduce heat to medium and cook till lightly brown stirring constantly.",
        "Reduce heat to medium-low and gradually incorporate other spices.",
        "Cook about 10-20 minutes until desired consistency.",
        "Makes enough sauce for 2 personal pans (two tortillas each) or 1 large pans (about 4-6 tortillas each).",
        "DO NOT USE COTIJA CHEESE IN THE ENCHILADAS.",
    )


default_recipe_registry.add_recipe(recipe=EnchiladaSauce())
