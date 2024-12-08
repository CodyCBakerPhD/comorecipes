from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class FriedRice(Recipe):
    name: str = "Fried Rice"
    tags: tuple[str, ...] = ("Asian",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="of chilled rice"),
        IngredientRegistry.get_measurement(amount=1, unit="serving", name="fried tofu"),
        IngredientRegistry.get_measurement(amount=2, unit="eggs", name=""),
        IngredientRegistry.get_measurement(amount=3, unit="tbsp.", name="butter"),
        IngredientRegistry.get_measurement(amount=3, unit="cloves", name="garlic"),
        IngredientRegistry.get_measurement(amount=1, unit="small", name="white onion"),
        IngredientRegistry.get_measurement(amount=1, unit="large", name="carrot"),
        IngredientRegistry.get_measurement(amount=1, unit="package", name="Shitake mushrooms"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="cup", name="frozen or fresh peas"),
        IngredientRegistry.get_measurement(amount=4, unit="tbsp.", name="soy sauce"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", name="sesame oil"),
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
