from ..._base._base_measurement import Measurement
from ..._base._base_recipe import Recipe
from ..._registration._ingredient_registry import IngredientRegistry
from ..._registration._recipe_registry import default_recipe_registry


class GingerbreadCookies(Recipe):
    name: str = "Gingerbread Cookies"
    tags: tuple[str, ...] = ("Christmas", "Vegetarian", "Dessert")
    measurements: tuple[Measurement, ...] = (
        IngredientRegistry.get_measurement(amount=180, unit="grams", ingredient_name="flour"),
        IngredientRegistry.get_measurement(amount=80, unit="grams", ingredient_name="dark brown sugar"),
        IngredientRegistry.get_measurement(amount=2, unit="grams", ingredient_name="baking soda"),
        IngredientRegistry.get_measurement(amount=4, unit="grams", ingredient_name="cinnamon"),
        IngredientRegistry.get_measurement(amount=2.5, unit="grams", ingredient_name="ginger"),
        IngredientRegistry.get_measurement(amount=0.5, unit="grams", ingredient_name="cloves"),
        IngredientRegistry.get_measurement(amount=1.5, unit="grams", ingredient_name="salt"),
        IngredientRegistry.get_measurement(amount=85, unit="grams", ingredient_name="butter"),
        IngredientRegistry.get_measurement(amount=125, unit="grams", ingredient_name="molasses"),
        IngredientRegistry.get_measurement(amount=15, unit="grams", ingredient_name="whole milk"),
    )
    instructions: tuple[str, ...] = (
        "### Dough",
        "Add flour, brown sugar, baking soda, cinnamon, ginger, cloves and salt to a mixing bowl and mix.",
        "Cut the butter into pieces and add to bowl, mixing until the mixture resembles fine meal.",
        "With mixer running on low speed gradually add the molasses and milk and mix until combined, about 30 seconds.",
        "Divide the dough in half, forming each into a ball.",
        "Wrap each in plastic wrap and refrigerate for at least 2 hours, until firm.",
        "### Baking",
        "Preheat the oven to 350 F.",
        "Line 2 baking sheets with parchment paper.",
        "Remove one dough sheet from the refrigerator and place on a well floured counter.",
        "Lightly flour the top of the dough and the rolling pin and roll out the dough.",
        "Roll until to a half inch thickness.",
        "Cut gingerbread men and place them on prepared baking sheets.",
        "Refrigerate the gingerbread men for 5 minutes.",
        "Bake for 8 to 11 minutes.",
        "Remove the cookies to a wire rack.",
        "Allow to cool to room temperature before frosting.",
    )
    notes: tuple[str, ...] = (
        "Refrigeration is mandatory or the dough will be too sticky to handle",
        "Be wary of overbaking as the darker color makes it difficult to tell."
        "One way to tell baking point is when cookie barely retains an imprint when touched gently with fingertip.",
    )


default_recipe_registry.add_recipe(recipe=GingerbreadCookies())
