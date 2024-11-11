from ..._base_recipe import Recipe
from ..._base_measurement import Measurement
from ..._recipe_registration import default_recipe_registry
from ..._measurement_registration import MeasurementRegistry


class ChocolateChipCookies(Recipe):
    name: str = "Chocolate Chip Cookies"
    measurements: list[Measurement] = [
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="room-temperature butter"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="sugar"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="cup", name="brown sugar"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="eggs", name=""),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tsp.", name="vanilla"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tsp.", name="baking soda"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tsp.", name="hot water"),
        MeasurementRegistry.get_measurement(amount=3.0, unit="cup", name="flour"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp.", name="salt"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="cups", name="high-quality semi-sweet chocolate chips"),
    ]
    instructions: list[str] = [
        "Oven temperature is 360 °F for caramelization stage.",
        "Cream together butter and sugars. Mix in one egg at a time. Add vanilla at the end.",
        "Dissolve baking soda in water and add to mixture. Mix together flour and salt separately, then add to wet mixture. Do not overwork.",
        "The tricky thing is getting the flour right; could be anywhere between 2 1/2 - 4 cups depending on how buttery/firm you want the result to be.",
        "Dough should be light and fluffy but not sticky.",
        "Baking time can also vary around ~12 minutes; watch your first batch carefully and adjust as needed.",
    ]


default_recipe_registry.add_recipe(recipe=ChocolateChipCookies())
