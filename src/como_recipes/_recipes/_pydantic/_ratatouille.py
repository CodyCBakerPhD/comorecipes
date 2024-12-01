from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class Ratatouille(Recipe):
    name: str = "Ratatouille"
    tags: tuple[str, ...] = "French"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=1, unit="serving", name="of piperade sauce"),
        MeasurementRegistry.get_measurement(amount=1, unit="small", name="eggplant, trimmed and thinly sliced"),
        MeasurementRegistry.get_measurement(amount=1, unit="zucchini,", name="trimmed and thinly sliced"),
        MeasurementRegistry.get_measurement(amount=1, unit="yellow", name="squash, trimmed and thinly sliced"),
        MeasurementRegistry.get_measurement(amount=2, unit="aloha", name="peppers, trimmed and thinly sliced"),
        MeasurementRegistry.get_measurement(amount=3, unit="tbsp.", name="olive oil"),
        MeasurementRegistry.get_measurement(amount=3, unit="tbsp.", name="mascarpone cheese"),
    )
    instructions: tuple[str, ...] = (
        "Make piperade sauce ahead of time.",
        "Recommend using mandolin for slicing main vegetables. Wear safety gloves!",
        "Preheat to 325 F.",
        "On top of sauce, assemble sliced vegetables in artistic fashion. Drizzle with olive oil.",
        "Bake for ~45 minutes.",
        "Remember, anyone can cook!",
    )


default_recipe_registry.add_recipe(recipe=Ratatouille())
