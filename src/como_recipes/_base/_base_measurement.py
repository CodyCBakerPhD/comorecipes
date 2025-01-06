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
    unit : typing.Literal["portions", "grams"]
        Unit of the ingredient amount.
    ingredient : Ingredient
        Ingredient being measured.
    prefix : str, optional
        Prefix to be added to the rendered text of the ingredient in a recipe.
        For example, "minced" for the ingredient "garlic".
    suffix : str, optional
        Suffix to be added to the rendered text of the ingredient in a recipe.
        For example, ", room-temperature" for the ingredient "butter".

    """

    amount: float | int | fractions.Fraction | typing.Literal["enough"]
    # TODO: limit to grams-base only
    unit: str | None
    # unit: typing.Literal["portions", "grams"]
    ingredient: Ingredient
    prefix: str | None = None
    suffix: str | None = None
    model_config = pydantic.ConfigDict(extra="forbid")

    def __init__(self, *args: list[typing.Any], **kwargs: dict[typing.Any, typing.Any]) -> None:
        if len(args) > 0:
            message = "No positional arguments are allowed."

            raise ValueError(message)

        amount = kwargs.get("amount", None)
        unit = kwargs.get("unit", None)

        if unit is None and amount != "enough":
            message = 'If `unit` is missing, `amount` must be "enough".'

            raise ValueError(message)

        if amount == "enough" and unit is not None:
            message = 'If `amount` is "enough", `unit` cannot be specified.'

            raise ValueError(message)

        if amount is not None and amount != "enough":
            amount = fractions.Fraction(amount).limit_denominator()

        kwargs["amount"] = amount
        kwargs["unit"] = unit

        super().__init__(**kwargs)

    def __repr__(self) -> str:
        """
        Logic defining the `repr` operator, most commonly used by printout of variables in Python/iPython shells.

        This is intended to be as programmatic (machine-readable) as possible; a user ought to be able to copy and paste
        the representation and run it as code to generate a new instance of the object.

        As a style choice, the representation is padded before and after with empty space.
        """
        if self.amount == "enough":
            string_amount = "enough"
        elif isinstance(self.amount, fractions.Fraction):
            string_amount = str(self.amount.numerator) if self.amount.denominator == 1 else str(self.amount)
        else:
            string_amount = str(self.amount)

        representation = f'Measurement(amount={string_amount}, unit="{self.unit}"'

        if self.prefix is not None:
            representation += f", prefix={self.prefix})"

        representation += f", ingredient={self.ingredient!r}"

        if self.suffix is not None:
            representation += f", suffix={self.suffix})"

        representation += ")"

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
