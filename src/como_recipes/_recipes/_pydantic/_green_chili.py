from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class GreenChili(Recipe):
    name: str = "Green Chili"
    tags: tuple[str, ...] = ("Mexican",)
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1, unit="tbps.", name="butter"),
        IngredientRegistry.get_measurement(amount=1, unit="large", name="white onion"),
        IngredientRegistry.get_measurement(amount=1, unit="qt.", name="of tomatoes"),
        IngredientRegistry.get_measurement(amount=10, unit="Anaheim", name="chilis"),
        IngredientRegistry.get_measurement(amount=2, unit="Jalepeno", name="peppers"),
        IngredientRegistry.get_measurement(amount=2, unit="tsp.", name="salt & pepper"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tbsp.", name="powdered mustard"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", name="dried oregano"),
        IngredientRegistry.get_measurement(amount=1, unit="tsp.", name="garlic powder"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", name="butter"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", name="flour"),
    )
    instructions: tuple[str, ...] = (
        "Grill the Anaheim peppers ahead of time; when skin is blackened, place into plastic bag and leave to cool.",
        "Remove skins and set aside.",
        "Dice the onion and Jalapeno peppers.",
        "Heat butter over medium-high heat until foamy, then saute onion.",
        "Add tomatoes, chilis, Jalepeno peppers, and spices.",
        "Bring to simmer then lower heat and continue simmering for 15 minutes.",
        "Make a roux with the remaining butter and flour; slowly mix chili into roux while stirring constantly to thicken.",
        "Serve with warm fresh tortillas.",
    )


default_recipe_registry.add_recipe(recipe=GreenChili())
