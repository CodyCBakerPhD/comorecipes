from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class Ratatouille(Recipe):
    name: str = "Ratatouille"
    tags: tuple[str, ...] = ("French", "Vegetarian", "Entree")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="serving", ingredient_name="of piperade sauce"),
        IngredientRegistry.get_measurement(
            amount=1,
            unit="small",
            ingredient_name="eggplant, trimmed and thinly sliced",
        ),
        IngredientRegistry.get_measurement(amount=1, unit="zucchini,", ingredient_name="trimmed and thinly sliced"),
        IngredientRegistry.get_measurement(
            amount=1,
            unit="yellow",
            ingredient_name="squash, trimmed and thinly sliced",
        ),
        IngredientRegistry.get_measurement(
            amount=2,
            unit="aloha",
            ingredient_name="peppers, trimmed and thinly sliced",
        ),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp.", ingredient_name="olive oil"),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp.", ingredient_name="mascarpone cheese"),
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
