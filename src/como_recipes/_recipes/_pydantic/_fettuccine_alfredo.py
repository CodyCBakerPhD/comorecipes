from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class FettuccineAlfredo(Recipe):
    name: str = "Fettuccine Alfredo"
    measurements: tuple[Measurement] = (
        MeasurementRegistry.get_measurement(amount=3.0, unit="eggs", name="worth of fettuccine noodles"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="cup", name="butter"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="heavy cream"),
        MeasurementRegistry.get_measurement(amount=3.0, unit="cloves", name="crushed garlic"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="1/2", name="cups freshly grated Parmesan"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tbsp.", name="fresh parsley"),
    )
    instructions: tuple[str] = (
        "Melt butter in saucepan over medium heat.",
        "Add cream and garlic, simmer for 5 minutes.",
        "Add most of the cheese, whisk quickly.",
        "Add rest of cheese just before serving.",
        "Garnish with the parsley if desired.",
    )


default_recipe_registry.add_recipe(recipe=FettuccineAlfredo())
