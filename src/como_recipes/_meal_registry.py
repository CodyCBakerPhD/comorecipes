import pathlib

import pydantic

from ._base_meal import Meal


class MealRegistry(pydantic.BaseModel):
    """A collection of meals that can be used to generate a shopping list."""

    meals: tuple[Meal, ...]

    def __len__(self) -> int:
        """Return the number of meals in the registry."""
        return len(self.meals)

    def get_shopping_list(self) -> list[str]:
        """Return a string representation of the shopping list."""

    def from_yaml(self, file_path: pathlib.Path) -> None:
        """Load meals from a YAML file."""

    def to_yaml(self, file_path: pathlib.Path) -> None:
        """Save meals to a YAML file."""
