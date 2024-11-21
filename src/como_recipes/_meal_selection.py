import collections
import typing

import pydantic

from ._measurement_registration import MeasurementRegistry


class MealSelector(pydantic.BaseModel):
    _recipe_names_by_tag: dict[typing.Literal["entree", "side", "dessert"], list[str]] | None = None
    _measurement_registry: MeasurementRegistry | None = None

    def __init__(self, *args: list[typing.Any], **kwargs: dict[typing.Any, typing.Any]) -> None:
        if len(args) > 0:
            message = "No positional arguments are allowed."
            raise ValueError(message)

        super().__init__(**kwargs)

        self._recipe_names_by_tag = collections.defaultdict(list, self._recipe_names_by_tag or {})
        self._measurement_registry = MeasurementRegistry()

    def __len__(self) -> int:
        combined_measurements = self._calculate_combined_measurements()
        return len(combined_measurements)

    def __repr__(self) -> str:
        number_of_registered_measurements = len(self)

        printout = f"{number_of_registered_measurements} registered measurements\n"

        if number_of_registered_measurements == 0:
            return printout

        printout += f"{'-' * (len(printout) - 1)}\n\n"
        printout += self._printout_nested_measurements()

        return printout

    def __str__(self) -> str:
        """Used by calls to `print(...)`."""
        return repr(self)

    def add_recipe(self, *, recipe_name: str) -> None:
        self._measurement_registry.add_recipe(recipe_name=recipe_name)
