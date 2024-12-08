import fractions
import typing

import pydantic

from ._base_ingredient import Ingredient


class Measurement(pydantic.BaseModel):
    """
    A measurement is a specified amount of an ingredient.

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

    amount: float | int | fractions.Fraction
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

    def __init__(self, *args: list[typing.Any], **kwargs: dict[typing.Any, typing.Any]) -> typing.Self:
        if len(args) > 0:
            message = "No positional arguments are allowed."
            raise ValueError(message)

        super().__init__(**kwargs)

        self.amount = fractions.Fraction(self.amount).limit_denominator()

    def __repr__(self) -> str:
        string_amount = str(self.amount.numerator) if self.amount.denominator == 1 else str(self.amount)
        representation = f'Measurement(amount={string_amount}, unit="{self.unit}", ingredient={self.ingredient!r})'

        return representation

    def __str__(self) -> str:
        """Used by calls to `print(...)`."""
        return repr(self)
