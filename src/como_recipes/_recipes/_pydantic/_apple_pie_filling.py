from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class ApplePieFilling(Recipe):
    name: str = "Apple Pie Filling"
    tags: tuple[str, ...] = ("American", "Dessert", "Pie", "Vegetarian", "Fruit")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="Pie", ingredient_name="crust"),
        IngredientRegistry.get_measurement(amount=3, unit="lbs.", ingredient_name="(about 5) Granny Smith apples"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="brown sugar"),
        IngredientRegistry.get_measurement(amount=1, unit="tbsp.", ingredient_name="lemon juice"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp.", ingredient_name="cinnamon"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="nutmeg"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", ingredient_name="flour"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", ingredient_name="raw sugar"),
    )
    instructions: tuple[str, ...] = (
        "Peel and core apples; slice thinly. Toss apples with all dry ingredients except raw sugar. Cover and refrigerate for at least 4 hours.",
        "Drain and reserve liquid in a small saucepan; bring liquid to simmer and reduce by half (stir constantly).",
        "Pour over apples and toss to combine. Pour into pie crust and seal. Sprinkle with raw sugar.",
        "Bake to pie crust instructions.",
    )


default_recipe_registry.add_recipe(recipe=ApplePieFilling())
