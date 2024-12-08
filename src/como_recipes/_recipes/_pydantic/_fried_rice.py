from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class FriedRice(Recipe):
    name: str = "Fried Rice"
    tags: tuple[str, ...] = ("Asian",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="serving", ingredient_name="of chilled rice"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", ingredient_name="fried tofu"),
        IngredientRegistry.get_measurement(amount=2, unit="eggs", ingredient_name=""),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp.", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=3, unit="cloves", ingredient_name="garlic"),
        IngredientRegistry.get_measurement(amount=1, unit="small", ingredient_name="white onion"),
        IngredientRegistry.get_measurement(amount=1, unit="large", ingredient_name="carrot"),
        IngredientRegistry.get_measurement(amount=1, unit="package", ingredient_name="Shitake mushrooms"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", ingredient_name="frozen or fresh peas"),
        IngredientRegistry.get_measurement(amount=4, unit="tbsp.", ingredient_name="soy sauce"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="sesame oil"),
    )
    instructions: tuple[str, ...] = (
        "Make and chill rice a day ahead of time.",
        "Fry tofu at same time.",
        "Scramble eggs and set aside.",
        "Stiry fry onion and garlic.",
        "Add other vegetables until cooked.",
        "Add rice and seasonings, fry until ready.",
    )


default_recipe_registry.add_recipe(recipe=FriedRice())
