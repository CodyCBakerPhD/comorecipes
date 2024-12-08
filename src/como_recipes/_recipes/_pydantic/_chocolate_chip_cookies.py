from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class ChocolateChipCookies(Recipe):
    name: str = "Chocolate Chip Cookies"
    tags: tuple[str, ...] = ("American",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="cup", name="room-temperature butter"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", name="sugar"),
        IngredientRegistry.get_measurement(amount=1, unit="cup", name="brown sugar"),
        IngredientRegistry.get_measurement(amount=2, unit="large", name="egg"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp.", name="vanilla"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", name="baking soda"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp.", name="hot water"),
        IngredientRegistry.get_measurement(amount=3, unit="cup", name="flour"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", name="salt"),
        IngredientRegistry.get_measurement(amount=2, unit="cups", name="high-quality semi-sweet chocolate chips"),
    )
    instructions: tuple[str, ...] = (
        "Oven temperature is 360 F for caramelization stage.",
        "Cream together butter and sugars. Mix in one egg at a time. Add vanilla at the end.",
        "Dissolve baking soda in water and add to mixture. Mix together flour and salt separately, then add to wet mixture. Do not overwork.",
        "The tricky thing is getting the flour right; could be anywhere between 2 1/2 - 4 cups depending on how buttery/firm you want the result to be.",
        "Dough should be light and fluffy but not sticky.",
        "Baking time can also vary around ~12 minutes; watch your first batch carefully and adjust as needed.",
    )


default_recipe_registry.add_recipe(recipe=ChocolateChipCookies())
