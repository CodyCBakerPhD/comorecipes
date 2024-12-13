from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class SauteedGreenBeans(Recipe):
    name: str = "Sauteed Green Beans"
    tags: tuple[str, ...] = ("American", "Side", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="bag", ingredient_name="fresh green beans"),
        IngredientRegistry.get_measurement(
            amount=1,
            unit="enough",
            ingredient_name="olive oil",
        ),  # TODO: relax this constraint
        IngredientRegistry.get_measurement(
            amount=1,
            unit="enough",
            ingredient_name="salt & pepper",
        ),  # So it can be "to taste"
    )
    instructions: tuple[str, ...] = (
        "Coat the bottom of a cast iron skillet with olive oil. Warm oil at medium heat.",
        "Add green beans, stirring to coat with olive oil.",
        "Add salt and pepper to taste, and stir again.",
        "Cover cast iron skillet with a lid, and cook for approximately 8 minutes, stirring occasionally.",
        "When green beans are crisping on the outside, reduce heat to low and continue cooking for ~5 minutes.",
    )


default_recipe_registry.add_recipe(recipe=SauteedGreenBeans())
