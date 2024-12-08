from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class CornbreadDressing(Recipe):
    name: str = "Cornbread Dressing"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=2, unit="portions", name="of cornbread"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp", name="butter"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", name="chopped celery"),
        IngredientRegistry.get_measurement(amount=1, unit="small", name="white onion"),
        IngredientRegistry.get_measurement(amount=2, unit="cups", name="not-chicken stock"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp", name="dried sage"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", name="salt"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", name="pepper"),
    )
    instructions: tuple[str, ...] = (
        "Make cornbread 1-2 days in advance, crumble and leave to dry. Melt butter and saute celery and onion until soft.",
        "Combine with cornbread. If not stuffing into turkey, then incorporate stock and spices. If stuffing, only incorporate the spices.",
        "Bake for 30 minutes at 350 F.",
    )


default_recipe_registry.add_recipe(recipe=CornbreadDressing())
