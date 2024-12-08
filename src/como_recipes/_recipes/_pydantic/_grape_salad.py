from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class GrapeSalad(Recipe):
    name: str = "Grape Salad"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=8, unit="oz.", name="cream cheese, softened"),
        IngredientRegistry.get_measurement(amount=8, unit="oz.", name="sour cream"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp", name="vanilla extract"),
        IngredientRegistry.get_measurement(amount=2, unit="lb", name="red seedless grapes"),
        IngredientRegistry.get_measurement(amount=2, unit="lbs", name="green seedless grapes"),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp", name="brown sugar"),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp", name="chopped pecans"),
    )
    instructions: tuple[str, ...] = (
        "In a large bowl, beat the cream cheese, sour cream, sugar and vanilla until blended. Add grapes and toss to coat.",
        "Transfer to a serving bowl. Cover and refrigerate until serving. Sprinkle with brown sugar and pecans just before serving",
        "Note: Makes 21-24 servings",
    )


default_recipe_registry.add_recipe(recipe=GrapeSalad())
