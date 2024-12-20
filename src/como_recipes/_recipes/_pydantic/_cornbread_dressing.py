from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class CornbreadDressing(Recipe):
    name: str = "Cornbread Dressing"
    tags: tuple[str, ...] = ("American", "Side", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=2, unit="portions", ingredient_name="of cornbread"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="chopped celery"),
        IngredientRegistry.get_measurement(amount=75, unit="grams", ingredient_name="white onion"),
        IngredientRegistry.get_measurement(amount=2, unit="cups", ingredient_name="not-chicken stock"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp", ingredient_name="dried sage"),
        IngredientRegistry.get_measurement(amount=3, unit="grams", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", ingredient_name="pepper"),
    )
    instructions: tuple[str, ...] = (
        "Make cornbread 1-2 days in advance, crumble and leave to dry. Melt butter and saute celery and onion until soft.",
        "Combine with cornbread. If not stuffing into turkey, then incorporate stock and spices. If stuffing, only incorporate the spices.",
        "Bake for 30 minutes at 350 F.",
    )


default_recipe_registry.add_recipe(recipe=CornbreadDressing())
