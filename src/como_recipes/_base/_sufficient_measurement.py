import typing

import pydantic

from ._base_ingredient import Ingredient
from ._base_measurement import Measurement


class SufficientMeasurement(Measurement):
    """
    A generic measurement used to indicate small or subjective quantities.

    Examples include salt and pepper for seasoning or oil for greasing a pan.

    Parameters
    ----------
    amount : typing.Literal["enough"]
        Amount of the ingredient.
    unit : None
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

    amount: typing.Literal["enough"] = "enough"
    unit: None = None
    prefix: str | None = None
    ingredient: Ingredient
    suffix: str | None = None
    model_config = pydantic.ConfigDict(extra="forbid")

    def __repr__(self) -> str:
        """
        Logic defining the `repr` operator, most commonly used by printout of variables in Python/iPython shells.

        This is intended to be as programmatic (machine-readable) as possible; a user ought to be able to copy and paste
        the representation and run it as code to generate a new instance of the object.

        As a style choice, the representation is padded before and after with empty space.
        """
        representation_lines = ['Measurement(amount="enough", unit=None']

        if self.prefix is not None:
            representation_lines += [f", prefix={self.prefix})"]

        representation_lines += [f", ingredient={self.ingredient!r}"]

        if self.suffix is not None:
            representation_lines += [f", suffix={self.suffix})"]

        representation_lines += [")"]

        representation = "".join(representation_lines)
        return representation

    def __str__(self) -> str:
        """
        Logic defining the `str` operator, which occurs either on casting to a string or when `print(...)` is called.

        This is intended to be as human-readable as possible.

        As a style choice, the printout is padded before and after with empty space.
        """
        return repr(self)
