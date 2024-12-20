from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class MacaroniAndCheese(Recipe):
    name: str = "Macaroni And Cheese"
    tags: tuple[str, ...] = ("American", "Vegetarian", "Entree", "Pasta")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=8, unit="oz.", ingredient_name="elbow pasta"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=30, unit="grams", ingredient_name="flour"),
        IngredientRegistry.get_measurement(
            amount=2,
            unit="cups",
            ingredient_name="of any combination between 2% milk (for thin consistency) and heavy cream (very thick texture)",
        ),
        IngredientRegistry.get_measurement(amount=7, unit="oz.", ingredient_name="English aged cheddar"),
        IngredientRegistry.get_measurement(amount=3 / 4, unit="tsp", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp", ingredient_name="pepper"),
        IngredientRegistry.get_measurement(amount=1, unit="grams", ingredient_name="paprika"),
    )
    instructions: tuple[str, ...] = (
        "Cook pasta ahead of time. Cut 75% of cheese into small cubes or shred. Shred remaining 25%.",
        "Melt butter and slowly whisk in flour. Do not cook too much.",
        "Slowly whisk in milk or cream. When mixture is warm, thoroughly melt 75% of cheese.",
        "Season.",
        "Mix pasta into mixture. Layer into dish, sprinkling remaining 25% of cheese across layers, leaving some for the top.",
        "Bake for 15 minutes at 325 F; optionally, broil the top for added flavor and texture.",
    )


default_recipe_registry.add_recipe(recipe=MacaroniAndCheese())
