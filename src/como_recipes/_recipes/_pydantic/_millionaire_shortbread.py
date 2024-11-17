from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class MillionareShortbread(Recipe):
    name: str = "Millionare Shortbread"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=1.0, unit="recipes", name="worth of shortbread"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="recipes", name="worth of simple caramel"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="recipes", name="worth of chocolate ganache"),
    ]
    instructions: list[str] = [
        "Make shortbread, let cool at least 15 minutes.",
        "Make simple caramel, and spread over shortbread. Let cool for several hours at room temperature or 1 hour in refrigerator.",
        "Make chocolate ganache, spread over caramel. Allow to harden before cutting.",
    ]


default_recipe_registry.add_recipe(recipe=MillionareShortbread())
