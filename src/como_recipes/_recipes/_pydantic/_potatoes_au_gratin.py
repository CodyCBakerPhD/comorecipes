from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class PotatoesAuGratin(Recipe):
    name: str = "Potatoes Au Gratin"
    tags: tuple[str, ...] = ("French", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=4, unit="russet", ingredient_name="potatoes"),
        IngredientRegistry.get_measurement(amount=1, unit="large", ingredient_name="onion"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="salt and pepper"),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp.", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp.", ingredient_name="flour"),
        IngredientRegistry.get_measurement(amount=2, unit="cups", ingredient_name="whole milk"),
        IngredientRegistry.get_measurement(amount=3 / 2, unit="cup", ingredient_name="cheddar"),
    )
    instructions: tuple[str, ...] = (
        "Preheat to 400 F. Butter the casserole dish.",
        "Layer 1/2 of potatoes into bottom of dish. Top with onions and add remaining potatoes. Season with salt and pepper.",
        "In medium-sized pan, melt butter over medium heat. Mix in flour and salt. Stir constantly with whisk for 1 minute. Stir in milk.",
        "Cook until thickened, then stir in cheese all at once.",
        "Continue stirring until melted, about 30 to 60 seconds. Pour cheese over potatoes and cover with dish with aluminum foil. Bake 90 minutes.",
    )


default_recipe_registry.add_recipe(recipe=PotatoesAuGratin())
