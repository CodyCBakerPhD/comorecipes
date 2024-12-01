from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class GreenChili(Recipe):
    name: str = "Green Chili"
    tags: tuple[str, ...] = ("Mexican",)
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1, unit="tbps.", name="butter"),
        MeasurementRegistry.get_measurement(amount=1, unit="large", name="white onion"),
        MeasurementRegistry.get_measurement(amount=1, unit="qt.", name="of tomatoes"),
        MeasurementRegistry.get_measurement(amount=10, unit="Anaheim", name="chilis"),
        MeasurementRegistry.get_measurement(amount=2, unit="Jalepeno", name="peppers"),
        MeasurementRegistry.get_measurement(amount=2, unit="tsp.", name="salt & pepper"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tbsp.", name="powdered mustard"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="dried oregano"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="garlic powder"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="cup", name="butter"),
        MeasurementRegistry.get_measurement(amount=1 / 4, unit="cup", name="flour"),
    )
    instructions: tuple[str, ...] = (
        "Grill the Anaheim peppers ahead of time; when skin is blackened, place into plastic bag and leave to cool.",
        "Remove skins and set aside.",
        "Dice the onion and Jalapeno peppers.",
        "Heat butter over medium-high heat until foamy, then saute onion.",
        "Add tomatoes, chilis, Jalepeno peppers, and spices.",
        "Bring to simmer then lower heat and continue simmering for 15 minutes.",
        "Make a roux with the remaining butter and flour; slowly mix chili into roux while stirring constantly to thicken.",
        "Serve with warm fresh tortillas.",
    )


default_recipe_registry.add_recipe(recipe=GreenChili())
