from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class SauteedGreenBeans(Recipe):
    name: str = "Sauteed Green Beans"
    tags: tuple[str, ...] = ("American", "Side")
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1, unit="bag", name="fresh green beans"),
        MeasurementRegistry.get_measurement(amount=1, unit="enough", name="olive oil"),  # TODO: relax this constraint
        MeasurementRegistry.get_measurement(amount=1, unit="enough", name="salt & pepper"),  # So it can be "to taste"
    )
    instructions: tuple[str, ...] = (
        "Coat the bottom of a cast iron skillet with olive oil. Warm oil at medium heat."
        "Add green beans, stirring to coat with olive oil."
        "Add salt and pepper to taste, and stir again."
        "Cover cast iron skillet with a lid, and cook for approximately 8 minutes, stirring occasionally."
        "When green beans are crisping on the outside, reduce heat to low and continue cooking for ~5 minutes."
    )


default_recipe_registry.add_recipe(recipe=SauteedGreenBeans())
