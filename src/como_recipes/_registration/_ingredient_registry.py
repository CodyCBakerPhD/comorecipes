import typing

import natsort
import pydantic

from .._base._base_ingredient import Ingredient
from .._base._base_measurement import Measurement


class IngredientRegistry(pydantic.BaseModel):
    """
    A registry of ingredients for use in recipes.

    The most useful part of this class is the static method `get_measurement`, which generates a `Measurement` object
    whose ingredient is either registered in the global default ingredient registry or is created on-the-fly.
    """

    _ingredients: dict[str, Ingredient] | None = None
    model_config = pydantic.ConfigDict(extra="forbid")

    def __init__(self, *args: list[typing.Any], **kwargs: dict[typing.Any, typing.Any]) -> None:
        if len(args) > 0:
            message = "No positional arguments are allowed."
            raise ValueError(message)

        super().__init__(**kwargs)

        self._ingredients = self._ingredients or {}

    def __len__(self) -> int:
        """
        Logic defining the `len` operator.

        Simply returns the number of registered ingredients.
        """
        return len(self._ingredients)

    def __contains__(self, item: str) -> bool:
        """
        Logic defining the `in` operator.

        E.g., `"Garlic" in ingredient_registry`

        Utilizing O(1) lookup is much faster than traditional iterative search.
        """
        return self._ingredients.get(item, None) is not None

    def __repr__(self) -> str:
        """
        Logic defining the `repr` operator, most commonly used by printout of variables in Python/iPython shells.

        This is intended to be as programmatic (machine-readable) as possible; a user ought to be able to copy and paste
        the representation and run it as code to generate a new instance of the object.

        As a style choice, the representation is padded before and after with empty space.
        """
        if len(self) == 0:
            return "\ncomo_recipes.IngredientRegistry()\n"

        representation = "\ncomo_recipes.IngredientRegistry(\n"
        representation += "\t_ingredients={"
        for _, ingredient in natsort.natsorted(seq=self._ingredients.items(), key=lambda item: item[0]):
            representation += f"\n\t\t{ingredient!r},"
        representation += "\n\t}\n"
        representation += ")\n"

        return representation

    def __str__(self) -> str:
        """
        Logic defining the `str` operator, which occurs either on casting to a string or when `print(...)` is called.

        This is intended to be as human-readable as possible.

        As a style choice, the printout is padded before and after with empty space.
        """
        number_of_registered_ingredients = len(self)

        printout = f"\n{number_of_registered_ingredients} registered ingredients\n"

        if number_of_registered_ingredients == 0:
            return printout

        printout += f"{'-' * (len(printout) - 1)}\n\n"
        for ingredient_name in natsort.natsorted(seq=self._ingredients.keys()):
            printout += f"{ingredient_name}\n"

        return printout

    @pydantic.validate_call
    def get_ingredient(self, *, ingredient_name: str) -> Ingredient:
        """
        Get an ingredient from the registry by name; returns a default base Ingredient if unregistered.

        Parameters
        ----------
        ingredient_name : str
            Name of the ingredient.

        """
        ingredient = self._ingredients.get(ingredient_name, None)
        if ingredient is None:
            message = f"Ingredient '{ingredient_name}' not found in the registry."
            raise ValueError(message)
        return ingredient

    @pydantic.validate_call
    def add_ingredient(self, *, ingredient: Ingredient) -> None:
        """
        Add a custom ingredient to the registry.

        Parameters
        ----------
        ingredient : Ingredient
            Custom ingredient to add to the registry

        """
        self._ingredients[ingredient.name] = ingredient

    @pydantic.validate_call
    def remove_ingredient(self, *, ingredient_name: str) -> None:
        """
        Remove a recipe from the registry.

        Parameters
        ----------
        ingredient_name : str
            Name of the ingredient to remove from the registry.

        """
        self._ingredients.pop(ingredient_name)

    @staticmethod
    @pydantic.validate_call
    def get_measurement(*, amount: int | float, unit: str, ingredient_name: str) -> Measurement:
        """
        Generate a measurement of an ingredient from the default global ingredient registry.

        Uses a base Ingredient if it is unregistered.

        Parameters
        ----------
        amount : int | float
            Amount of the ingredient.
        unit : str
            Unit of the ingredient amount.
        ingredient_name : str
            Name of the ingredient.

        """
        if ingredient_name in default_ingredient_registry:
            ingredient = default_ingredient_registry.get_ingredient(ingredient_name=ingredient_name)
        else:
            ingredient = Ingredient(name=ingredient_name)

        return Measurement(amount=amount, unit=unit, ingredient=ingredient)


# Initialize the global default ingredient registry
# Items are explicitly added in their respective ingredient files
default_ingredient_registry = IngredientRegistry()
