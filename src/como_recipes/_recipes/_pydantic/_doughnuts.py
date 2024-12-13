from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class Doughnuts(Recipe):
    name: str = "Doughnuts"
    tags: tuple[str, ...] = ("American", "Dessert", "Vegetarian")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=1 / 8, unit="o.z", ingredient_name="activate dry yeast"),
        IngredientRegistry.get_measurement(amount=1 / 8, unit="cup", ingredient_name="warm water"),
        IngredientRegistry.get_measurement(amount=3 / 4, unit="cup", ingredient_name="lukewarm milk"),
        IngredientRegistry.get_measurement(amount=1 / 4, unit="cup", ingredient_name="sugar"),
        IngredientRegistry.get_measurement(amount=1 / 2, unit="tsp.", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=1, unit="large", ingredient_name="egg"),
        IngredientRegistry.get_measurement(amount=1 / 6, unit="cup", ingredient_name="shortening"),
        IngredientRegistry.get_measurement(amount=5 / 2, unit="cups", ingredient_name="all-purpose flour"),
        IngredientRegistry.get_measurement(amount=1, unit="qt.", ingredient_name="vegetable oil"),
        IngredientRegistry.get_measurement(amount=1 / 6, unit="cup", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=1, unit="cups", ingredient_name="powdered sugar"),
        IngredientRegistry.get_measurement(amount=3 / 4, unit="tsp.", ingredient_name="vanilla"),
        IngredientRegistry.get_measurement(amount=2, unit="tbsp.", ingredient_name="hot water"),
    )
    instructions: tuple[str, ...] = (
        "Activate yeast.",
        "In large bowl, mix together activated yeast, milk, sugar, salt, eggs, shortening, and 1 cup of the flour.",
        "Mix for a few minutes at low speed.",
        "Beat in remaining flour 1/2 cup at a time, until dough no longer sticks to the bowl.",
        "Knead by hand for 5 minutes until smooth and elastic.",
        "Prove until doubled, about an hour.",
        "Gently roll out to 1/2 inch thickness. Shape as desired.",
        "Cover with cloth and prove again until doubled, about 40 minutes.",
        "Heat oil to 350 F.",
        "Slide doughnuts into hot oil using a wide spatula.",
        "Turn over as they rise to the surface. Fry each side until golden brown.",
        "Drain and cool on wire rack.",
        "Melt the butter in a saucepan, incorporate sifted powdered sugar and vanilla.",
        "Dip doughnuts in glaze while still warm.",
    )


default_recipe_registry.add_recipe(recipe=Doughnuts())
