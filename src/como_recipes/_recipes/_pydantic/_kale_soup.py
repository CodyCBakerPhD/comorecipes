from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class KaleSoup(Recipe):
    name: str = "Kale Soup"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=2, unit="tbsp.", name="olive oil"),
        MeasurementRegistry.get_measurement(amount=1, unit="yellow", name="onion, chopped"),
        MeasurementRegistry.get_measurement(amount=2, unit="tbsp.", name="garlic, chopped"),
        MeasurementRegistry.get_measurement(amount=1, unit="bunch", name="of kale, stems removed and leaves chopped"),
        MeasurementRegistry.get_measurement(amount=8, unit="cups", name="water"),
        MeasurementRegistry.get_measurement(amount=6, unit="cubes", name="of vegetable bouillon"),
        MeasurementRegistry.get_measurement(amount=15, unit="oz.", name="stewed tomatoes"),
        MeasurementRegistry.get_measurement(amount=6, unit="white", name="potatoes, cubed"),
        MeasurementRegistry.get_measurement(amount=30, unit="oz", name="cannellini beans (two 15 oz. cans), drained"),
        MeasurementRegistry.get_measurement(amount=1, unit="tbsp.", name="Italian seasoning"),
        MeasurementRegistry.get_measurement(amount=2, unit="tbsp.", name="dried parsley"),
        MeasurementRegistry.get_measurement(amount=1, unit="tsp.", name="Salt and pepper"),
    )
    instructions: tuple[str, ...] = (
        "Heat olive oil in a large soup pot. Cook the onion and garlic until soft. Stir in the kale and cook until wilted (about 2 minutes).",
        "Stir in the water, bouillon, tomatoes, potatoes, beans, Italian seasoning, parsley.",
        "Simmer soup on medium heat for 25 minutes, or until potatoes are cooked through. Season with salt and pepper to taste.",
    )


default_recipe_registry.add_recipe(recipe=KaleSoup())
