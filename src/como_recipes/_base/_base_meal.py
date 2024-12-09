import typing

import pydantic

from ._base_recipe import Recipe
from ..utils import get_recipe_names_by_type


class Meal(pydantic.BaseModel):
    """
    A meal is a collection of recipes to be prepared and eaten together.

    Initialize an empty `Meal()` then call `Meal.add_recipe(recipe=...)` to add recipes to it.

    Parameters
    ----------
    quantity_multiplier : int | float | None
        Default recipes tend to be scaled to 2 people, plus or minus leftovers.
        If more people need to be fed, adjust this scale accordingly.

    """

    _recipe_name_to_recipe: dict[str, Recipe] | None = None
    quantity_multiplier: int | float | None = None
    model_config = pydantic.ConfigDict(extra="forbid")

    def __len__(self) -> int:
        """
        Logic defining the `len` operator.

        Simply returns the number of registered recipes.
        """
        return len(self._recipe_name_to_recipe)

    def __init__(self, *args: list[typing.Any], **kwargs: dict[typing.Any, typing.Any]) -> None:
        if len(args) > 0:
            message = "No positional arguments are allowed."
            raise ValueError(message)

        super().__init__(**kwargs)

        self._recipe_name_to_recipe = self._recipe_name_to_recipe or {}

    def __eq__(self, other: "Meal") -> bool:
        """Primary used by consistency assertions in the tests."""
        if self._recipe_name_to_recipe != other._recipe_name_to_recipe:
            return False
        if self.quantity_multiplier is None and other.quantity_multiplier is None:
            return True
        if self.quantity_multiplier != other.quantity_multiplier:
            return False
        return True

    def __repr__(self) -> str:
        """Used in programmatic places, such as equality assertions in the tests."""
        recipe_names = get_recipe_names_by_type(recipes=list(self._recipe_name_to_recipe.values()))

        representation = "como_recipes.Meal(\n\trecipes={\n"
        for recipe_name in recipe_names:
            representation += f'\t\tcomo_recipes.Recipe(name="{recipe_name}", ...),\n'
        representation += "\t}"
        if self.quantity_multiplier is not None:
            representation += ",\n"
            representation += f"\tquantity_multiplier={self.quantity_multiplier},\n"
        else:
            representation += "\n"
        representation += ")\n"

        return representation

    def __str__(self) -> str:
        """Used by calls to `print(...)`."""
        recipe_names = get_recipe_names_by_type(recipes=list(self._recipe_name_to_recipe.values()))

        printout = "Recipes\n"
        printout += "-------\n"
        if self.quantity_multiplier is None:
            for recipe_name in recipe_names:
                printout += f"{recipe_name}\n"
        else:
            for recipe_name in recipe_names:
                printout += f"{recipe_name} x{self.quantity_multiplier}\n"

        return printout

    def add_recipe(self, recipe: Recipe) -> None:
        """Add a recipe to the meal."""
        self._recipe_name_to_recipe[recipe.name] = recipe

    def remove_recipe(self, recipe_name: str) -> None:
        """Remove a recipe from the meal."""
        self._recipe_name_to_recipe.pop(recipe_name)

    def get_recipes_by_type(self) -> tuple[Recipe]:
        """Get all the recipes of this meal ordered by type (entree before side, alphabetically)."""
        recipe_names = get_recipe_names_by_type(recipes=list(self._recipe_name_to_recipe.values()))

        return tuple(self._recipe_name_to_recipe[recipe_name] for recipe_name in recipe_names)
