from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class Shortbread(Recipe):
    name: str = "Shortbread"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="cup", name="butter, room temperature"),
        IngredientRegistry.get_measurement(amount=1 / 3, unit="cup", name="sugar"),
        IngredientRegistry.get_measurement(amount=1 / 3, unit="cup", name="brown sugar"),
        IngredientRegistry.get_measurement(amount=1, unit="large", name="egg yolk"),
        IngredientRegistry.get_measurement(amount=3 / 4, unit="tsp.", name="vanilla extract"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", name="salt"),
        IngredientRegistry.get_measurement(amount=9 / 4, unit="cups", name="flour"),
    )
    instructions: tuple[str, ...] = (
        "Preheat oven to 350 F. Line a 13x9 baking pan with parchment paper.",
        "Using a stand mixer, beat butter until well creamed.",
        "Add sugars and beat until light and fluffy.",
        "Add egg yolk and vanilla extract. Combine well, scraping the sides.",
        "Add flour gradually, scraping the sides.",
        "Halfway through incorporating flour, sprinkle in salt.",
        "Do not overwork the dough.",
        "Drop dough over baking pan and evenly press onto bottom.",
        "Bake for about 23 minutes or until lightly golden brown.",
    )


default_recipe_registry.add_recipe(recipe=Shortbread())
