from ..._base import Recipe, MeasuredIngredient


class Applesauce(Recipe):
    name = "Applesauce"
    ingredients = [
        MeasuredIngredient(name="", amount=4.0, unit="apples"),
        MeasuredIngredient(name="water", amount=0.75, unit="cup"),
        MeasuredIngredient(name="white sugar", amount=0.0625, unit="cup"),
        MeasuredIngredient(name="brown sugar", amount=0.0625, unit="cup"),
        MeasuredIngredient(name="ground cinnamon", amount=0.5, unit="tsp."),
    ]
    instructions = [
        "Peel and core apples.",
        "Combine everything and cook over medium heat for 15-20 minutes (until apples are soft).",
        "Allow to cool, then mash with fork or potato masher.",
    ]
