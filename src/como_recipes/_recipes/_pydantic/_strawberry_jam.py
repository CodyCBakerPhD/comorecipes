from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class StrawberryJam(Recipe):
    name: str = "Strawberry Jam"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=3 / 2, unit="", ingredient_name="cups of thinly sliced strawberries"),
        IngredientRegistry.get_measurement(amount=40, unit="", ingredient_name="g. sugar"),
        IngredientRegistry.get_measurement(amount=40, unit="", ingredient_name="g. brown sugar"),
        IngredientRegistry.get_measurement(amount=20, unit="", ingredient_name="g. honey"),
        IngredientRegistry.get_measurement(amount=9 / 4, unit="tbsp.", ingredient_name="cornstarch"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="", ingredient_name="tsp. vanilla extract"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="lime juice"),
    )
    instructions: tuple[str, ...] = (
        "Carefully weigh the white and brown sugar into a small bowl.",
        "Save adding honey this mixture until just ready to add to strawberries.",
        "Heat strawberries slowly over medium-low heat stirring constantly, until juices begin leaking.",
        "Then quickly incorporate the sugars and cornstarch and stir well until everything is homogeneous.",
        "Increase heat to just above medium, and reach a boil stirring often.",
        "When mixture is at boil (it remains boiling upon stirring) then stir constantly for one minute and then remove from heat.",
        "Let cool before using.",
    )


default_recipe_registry.add_recipe(recipe=StrawberryJam())
