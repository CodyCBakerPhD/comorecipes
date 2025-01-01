import fractions
import typing

import pydantic

from ._base_ingredient import Ingredient


class Measurement(pydantic.BaseModel):
    """
    A measurement is a specified amount of an ingredient.

    Parameters
    ----------
    amount : int | float | typing.Literal["enough"]
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

    amount: float | int | fractions.Fraction | typing.Literal["enough"]
    # TODO: limit to grams-base only
    unit: str | None
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
    model_config = pydantic.ConfigDict(extra="forbid")

    def __init__(self, *args: list[typing.Any], **kwargs: dict[typing.Any, typing.Any]) -> typing.Self:
        if len(args) > 0:
            message = "No positional arguments are allowed."

            raise ValueError(message)

        if kwargs.get("unit", None) is None and kwargs.get("amount", "") != "enough":
            message = 'If `unit` is missing, `amount` must be "enough".'

            raise ValueError(message)

        if kwargs.get("amount", "") == "enough" and kwargs.get("unit", None) is not None:
            message = 'If `amount` is "enough", `unit` cannot be specified.'

            raise ValueError(message)

        super().__init__(**kwargs)

        self.amount = fractions.Fraction(self.amount).limit_denominator()

    def __repr__(self) -> str:
        """
        Logic defining the `repr` operator, most commonly used by printout of variables in Python/iPython shells.

        This is intended to be as programmatic (machine-readable) as possible; a user ought to be able to copy and paste
        the representation and run it as code to generate a new instance of the object.

        As a style choice, the representation is padded before and after with empty space.
        """
        string_amount = str(self.amount.numerator) if self.amount.denominator == 1 else str(self.amount)
        representation = f'Measurement(amount={string_amount}, unit="{self.unit}", ingredient={self.ingredient!r})'

        return representation

    def __str__(self) -> str:
        """
        Logic defining the `str` operator, which occurs either on casting to a string or when `print(...)` is called.

        This is intended to be as human-readable as possible.

        As a style choice, the printout is padded before and after with empty space.
        """
        return repr(self)

    def __eq__(self, other: "Measurement") -> bool:
        """
        Logic defining the `==` operator.

        Primarily used by consistency assertions in the tests.

        Compares only the contained fields of the object, not including its memory address (two imported instances
        of the class with the same fields will be considered equal).
        """
        fields_to_compare = ["amount", "unit", "ingredient"]
        result = all(getattr(self, field) == getattr(other, field) for field in fields_to_compare)

        return result
