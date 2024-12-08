from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class PotPie(Recipe):
    name: str = "Pot Pie"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="full", name="pie crust"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="of firm tofu"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", name="butter"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="medium", name="yellow onions, finely chopped"),
        IngredientRegistry.get_measurement(amount=2, unit="medium", name="carrots, peeled and finely chopped"),
        IngredientRegistry.get_measurement(amount=1, unit="small", name="russet potato, peeled and diced"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp.", name="salt and pepper"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", name="flour"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", name="not-chicken broth"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", name="whole milk"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", name="green peas"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cups", name="thinly sliced chives"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="cup", name="parsley"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", name="white vinegar"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp.", name="water"),
        IngredientRegistry.get_measurement(amount=1, unit="large", name="egg yolk"),
    )
    instructions: tuple[str, ...] = (
        "Make pie crust well ahead of time, make sure it's cold in the fridge.",
        "Preheat oven to 400 F.",
        "Firm up tofu even more by halving and baking for 10 minutes on parchment paper.",
        "Melt butter in heavy bottomed saucepan. When it foams, add onions and carrots and cook for 1-2 minutes.",
        "Add potato, season well with salt and black pepper. Stir to coat. Cook, stirring rarely, for about 6 minutes.",
        "Sprinkle flour over vegetables, stir to coat, and cook another 1-2 minutes.",
        "Carefully add broth and milk, stirring constantly until mixture is smooth. Bring to a simmer over medium heat and cook another 5 minutes.",
        "Remove from heat, add peas, herbs, and vinegar. Stir to coat. Season well with salt and pepper.",
        "Place bottom half of pie crust in dish, fill with mixture. Cover with other half and seal tightly. Whisk water and egg yolk, then wash the top. Cut slits in top to vent.",
        "Bake for 30 minutes. Let sit at least 5 minutes before serving.",
    )


default_recipe_registry.add_recipe(recipe=PotPie())
