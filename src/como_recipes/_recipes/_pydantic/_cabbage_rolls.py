from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class CabbageRolls(Recipe):
    name: str = "Cabbage Rolls"
    measurements: tuple[Measurement] = (
        MeasurementRegistry.get_measurement(amount=1.25, unit="cups", name="white rice"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="large", name="napa cabbage"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="white", name="onion"),
        MeasurementRegistry.get_measurement(amount=0.75, unit="tbsp.", name="ginger, minced"),
        MeasurementRegistry.get_measurement(amount=3.0, unit="cloves", name="garlic, minced"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="minced", name="carrot"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="minced", name="peppers"),
        MeasurementRegistry.get_measurement(amount=8.0, unit="minced", name="shittake mushrooms"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tbsp.", name="tamari"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="pepper"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="onion powder"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="tsp.", name="red pepper flakes"),
    )
    instructions: tuple[str] = (
        "Soak rice in bowl 60 minutes before cooking. Cook in 5/3 cup water and 1 tbsp. butter; reach boiling before reducing to simmer until all water is gone.",
        "Prep cabbage leaves by chopping off thickest bottom portion then boiling a large pot of water and adding 3-4 leaves at a time for 1 minute until softened. When done, place them into bowl of cold water and set aside.",
        "Heat some peanut oil in a skillet and saute vegetables for 4 minutes; then add tamari and remaining spices. Cook for another 2 minutes.",
        "Combine rice and vegetable mixture. Season to taste.",
        "To assemble, add about 1 tbsp. of mixture to a single cabbage leaf, fold and roll together.",
        "Pan sear the rolls in large skillet for a few minutes on all sides; rolls should be golden brown.",
        "Garnish with sesame seeds. Recommend topping with Tamari Sauce for extra flavor.",
    )


default_recipe_registry.add_recipe(recipe=CabbageRolls())
