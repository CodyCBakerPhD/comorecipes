"""Collection of minor help functions."""

import importlib.metadata
import pathlib
import sys

import natsort
import pydantic

from ._base._base_recipe import Recipe


def get_package_version() -> str:
    """Load the version hardcopy file."""
    # Must determine if path to asset is relative (in dev mode) or frozen (in production mode)
    is_bundled = hasattr(sys, "_MEIPASS")
    if is_bundled is True:
        base_path = pathlib.Path(sys._MEIPASS)  # noqa: SLF001

        file_path = base_path / "pyproject.toml"
        with file_path.open(mode="r") as io:
            lines = io.readlines()

        version_line = next(line for line in lines if "version" in line)
        version = version_line.split("=")[1].strip().strip('"')
    else:
        version = importlib.metadata.version(distribution_name="como_recipes")
    version_string = f"v{version}"

    return version_string


@pydantic.validate_call
def get_recipe_names_by_type(*, recipes: list[Recipe] | tuple[Recipe]) -> list[str]:
    """
    Common logic used by both `__repr__` and `__str__`.

    Fetch the recipe names in a deterministic order given alphabetically by tags (Entree vs. Side).
    """
    entrees = natsort.natsorted(seq=(recipe.name for recipe in recipes if "Entree" in recipe.tags))
    sides = natsort.natsorted(seq=(recipe.name for recipe in recipes if "Side" in recipe.tags))
    others = natsort.natsorted(seq=({recipe.name for recipe in recipes} - set(entrees) - set(sides)))
    recipe_names_by_type = entrees + sides + others

    return recipe_names_by_type
