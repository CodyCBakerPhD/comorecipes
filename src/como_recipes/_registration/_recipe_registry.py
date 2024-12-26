import pathlib
import typing

import natsort
import pydantic

from .._base._base_recipe import Recipe
from ..utils import get_bundle_base_path, is_bundled


class RecipeRegistry(pydantic.BaseModel):
    _recipes: dict[str, Recipe] | None = None
    model_config = pydantic.ConfigDict(extra="forbid")

    def __init__(self, *args: list[typing.Any], **kwargs: dict[typing.Any, typing.Any]) -> None:
        if len(args) > 0:
            message = "No positional arguments are allowed."
            raise ValueError(message)

        super().__init__(**kwargs)

        self._recipes = self._recipes or {}

    def __len__(self) -> int:
        """
        Logic defining the `len` operator.

        Simply returns the number of registered recipes.
        """
        return len(self._recipes)

    def __repr__(self) -> str:
        """
        Logic defining the `repr` operator, most commonly used by printout of variables in Python/iPython shells.

        This is intended to be as programmatic (machine-readable) as possible; a user ought to be able to copy and paste
        the representation and run it as code to generate a new instance of the object.

        As a style choice, the representation is padded before and after with empty space.
        """
        if len(self) == 0:
            return "\ncomo_recipes.RecipeRegistry()\n"

        representation = "\ncomo_recipes.RecipeRegistry(\n"
        representation += "\t_recipes={"
        for recipe_name, _ in natsort.natsorted(seq=self._recipes.items(), key=lambda item: item[0]):
            representation += f'\n\t\tcomo_recipes.Recipe(name="{recipe_name}", ...),'
        representation += "\n\t}\n"
        representation += ")\n"

        return representation

    def __str__(self) -> str:
        """
        Logic defining the `str` operator, which occurs either on casting to a string or when `print(...)` is called.

        This is intended to be as human-readable as possible.

        As a style choice, the printout is padded before and after with empty space.
        """
        number_of_registered_recipes = len(self)

        printout = f"{number_of_registered_recipes} registered recipes\n"

        if number_of_registered_recipes == 0:
            return printout

        printout += f"{'-' * (len(printout)-1)}\n\n"
        for recipe_name in natsort.natsorted(seq=self._recipes.keys()):
            printout += f"{recipe_name}\n"

        return printout

    @pydantic.validate_call
    def add_recipe(self, *, recipe: Recipe) -> None:
        """
        Add a recipe to the registry.

        Parameters
        ----------
        recipe : Recipe
            Recipe to add to the registry.

        """
        self._recipes[recipe.name] = recipe

    @pydantic.validate_call
    def remove_recipe(self, *, recipe_name: str) -> None:
        """
        Remove a recipe from the registry.

        Parameters
        ----------
        recipe_name : str
            Name of the recipe to remove from the registry.

        """
        self._recipes.pop(recipe_name)

    @pydantic.validate_call
    def get_recipe(self, *, recipe_name: str) -> Recipe:
        """
        Get a recipe from the registry.

        Parameters
        ----------
        recipe_name : str
            Name of the recipe to get from the registry.

        """
        recipe = self._recipes.get(recipe_name, None)
        if recipe is None:
            message = f"Recipe '{recipe_name}' not found in the registry."
            raise ValueError(message)
        return recipe

    @pydantic.validate_call
    def get_all_recipe_names(self) -> list[str]:
        """Get all recipes from the registry."""
        return list(self._recipes.keys())


# Initialize the global default recipe registry
# Items are explicitly added in their respective recipe files
default_recipe_registry = RecipeRegistry()

_recipe_directory = (
    pathlib.Path(__file__).parent.parent / "_recipes" if is_bundled() is False else get_bundle_base_path() / "_recipes"
)
for file_path in _recipe_directory.glob(pattern="*.yaml"):
    recipe = Recipe.from_yaml_file(file_path=file_path)
    default_recipe_registry.add_recipe(recipe=recipe)
