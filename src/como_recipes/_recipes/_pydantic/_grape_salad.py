from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class GrapeSalad(Recipe):
    name: str = "Grape Salad"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=8, unit="oz.", ingredient_name="cream cheese, softened"),
        IngredientRegistry.get_measurement(amount=8, unit="oz.", ingredient_name="sour cream"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp", ingredient_name="vanilla extract"),
        IngredientRegistry.get_measurement(amount=2, unit="lb", ingredient_name="red seedless grapes"),
        IngredientRegistry.get_measurement(amount=2, unit="lbs", ingredient_name="green seedless grapes"),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp", ingredient_name="brown sugar"),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp", ingredient_name="chopped pecans"),
    )
    instructions: tuple[str, ...] = (
        "In a large bowl, beat the cream cheese, sour cream, sugar and vanilla until blended. Add grapes and toss to coat.",
        "Transfer to a serving bowl. Cover and refrigerate until serving. Sprinkle with brown sugar and pecans just before serving",
        "Note: Makes 21-24 servings",
    )


default_recipe_registry.add_recipe(recipe=GrapeSalad())
