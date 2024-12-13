from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class HappyPlums(Recipe):
    name: str = "Happy Plums"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=4, unit="plums", ingredient_name=""),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="coconut oil"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="basalmic vinegar"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="tsp.", ingredient_name="vanilla extract"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="chopped fresh rosemary"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="honey"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="sour cream"),
    )
    instructions: tuple[str, ...] = (
        "Preheat oven to 350 F. Cut plums in half and remove the pits. Coat baking pan with oil. Brush plums with oil, then sprinkle a thin layer of sugar on each. Bake for 20 minutes.",
        "In a pot, combine basalmic vinegar and rosemary (Note: basalmic syrup is very stinky, ventilate well). Bring the mixture to a boil and lower to a simmer, reducing for about 8 minutes.",
        "Add honey and vanilla, stir until dissolved. Remove mixture from heat and strain the basalmic syrup to separate from the rosemary.",
    )


default_recipe_registry.add_recipe(recipe=HappyPlums())
