from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class MillionaireShortbread(Recipe):
    name: str = "Millionaire Shortbread"
    tags: tuple[str, ...] = ("British", "Dessert")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="recipes", name="worth of shortbread"),
        IngredientRegistry.get_measurement(amount=1, unit="recipes", name="worth of simple caramel"),
        IngredientRegistry.get_measurement(amount=1, unit="recipes", name="worth of chocolate ganache"),
    )
    instructions: tuple[str, ...] = (
        "Make shortbread, let cool at least 15 minutes.",
        "Make simple caramel, and spread over shortbread. Let cool for several hours at room temperature or 1 hour in refrigerator.",
        "Make chocolate ganache, spread over caramel. Allow to harden before cutting.",
    )


default_recipe_registry.add_recipe(recipe=MillionaireShortbread())
