from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class HoneyGarlicSalmon(Recipe):
    name: str = "Honey Garlic Salmon"
    tags: tuple[str, ...] = ("American", "Entree")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=4, unit="salmon", ingredient_name="fillets, 250 g each"),
        IngredientRegistry.get_measurement(amount=3, unit="grams", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp", ingredient_name="black pepper"),
        IngredientRegistry.get_measurement(amount=2, unit="grams", ingredient_name="paprika"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=4, unit="cloves", ingredient_name="garlic, finely chopped"),
        IngredientRegistry.get_measurement(amount=4, unit="tbsp", ingredient_name="honey"),
        IngredientRegistry.get_measurement(amount=15, unit="grams", ingredient_name="water"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp", ingredient_name="soy sauce"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp", ingredient_name="fresh lemon juice"),
        IngredientRegistry.get_measurement(amount=4, unit="lemon", ingredient_name="wedges to garnish"),
    )
    instructions: tuple[str, ...] = (
        "Move oven shelf to middle. Preheat to broil/grill settings on medium heat. Season salmon with salt, pepper, paprika. Set aside.",
        "Heat butter in a skillet over medium-high heat until melted. Add garlic and saute for a minute. Pour in honey, water, and soy sauce. Allow flavors to heat through.",
        "Add lemon juice, stir well to combine. Add the salmon to the sauce in the pan, cook each fillet for 3-4 minutes or until golden. Baste the tops with the pan juices.",
        "Season with salt and pepper to taste. Add lemon wedges around salmon if desired. Baste salmon one more time, transfer pan to the oven to broil/grill for 5-6 minutes.",
        "To serve, drizzle with sauce and a squeeze of lemon juice.",
    )


default_recipe_registry.add_recipe(recipe=HoneyGarlicSalmon())
