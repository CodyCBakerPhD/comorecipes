import pydantic

from ._base_ingredient import Ingredient


class Measurement(pydantic.BaseModel):
    """Automatically validated base data class for all measured portions of ingredients.

    Parameters
    ----------
    amount : int | float
        Amount of the ingredient.
    unit : Literal[
        "cup",
        "cups",
        "tbsp",
        "tsp",
        "oz",
        "lb",
        "g",
        "kg",
        "large",
        "tsp.",
        "tbsp.",
        "apples",
        "qt.",
        "lb.",
    ]
        Unit of the ingredient amount.
    ingredient : Ingredient
        Ingredient being measured.

    """

    amount: int | float
    # TODO: limit to grams-base only
    unit: str
    # unit: Literal[
    #     "cup",
    #     "cups",
    #     "tbsp",
    #     "tsp",
    #     "oz",
    #     "lb",
    #     "g",
    #     "grams",
    #     "kg",
    #     "large",
    #     "tsp.",
    #     "tbsp.",
    #     "apples",
    #     "qt.",
    #     "lb.",
    #     "Pie",
    #     "lbs.",
    #     "Good",
    #     "egg",
    #     "ripe",
    # ]
    ingredient: Ingredient
