from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class Falafel(Recipe):
    name: str = "Falafel"
    tags: tuple[str, ...] = ("Greek", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="lb.", ingredient_name="dry chickpeas"),
        IngredientRegistry.get_measurement(amount=1, unit="small", ingredient_name="white onion"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="parsley"),
        IngredientRegistry.get_measurement(amount=5, unit="gloves", ingredient_name="garlic"),
        IngredientRegistry.get_measurement(amount=3 / 2, unit="tbsp.", ingredient_name="flour"),
        IngredientRegistry.get_measurement(amount=7 / 4, unit="tsp.", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp.", ingredient_name="cumin"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", ingredient_name="coriander"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="pepper"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="tsp.", ingredient_name="cayenne"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="tsp.", ingredient_name="cardamom"),
    )
    instructions: tuple[str, ...] = (
        "Soak beans overnight.",
        "Grind entire mixture well in a food processor.",
        "Shape and deep fry at 375 F until golden brown.",
    )


default_recipe_registry.add_recipe(recipe=Falafel())
