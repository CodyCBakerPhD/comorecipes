from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class SauteedMushrooms(Recipe):
    name: str = "Sauteed Mushrooms"
    tags: tuple[str, ...] = ("American", "Side", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=3, unit="tbsp", ingredient_name="olive oil"),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=1, unit="lb.", ingredient_name="button mushrooms"),
        IngredientRegistry.get_measurement(amount=5, unit="grams", ingredient_name="garlic"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp", ingredient_name="red wine"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp", ingredient_name="garlic salt"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp", ingredient_name="pepper"),
    )
    instructions: tuple[str, ...] = (
        "Heat oil and butter in large saucepan over medium heat.",
        "Cook all ingredients until mushrooms are lightly browned.",
        "Reduce heat to low and simmer until mushrooms are tender, about 5-8 more minutes.",
    )


default_recipe_registry.add_recipe(recipe=SauteedMushrooms())
