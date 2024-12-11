"""Collection of minor help functions."""

import ctypes
import importlib.metadata
import pathlib
import struct
import sys

import natsort
import pydantic

from ._base._base_recipe import Recipe


def save_version_hardcopy() -> None:
    """
    When bundling with PyInstaller, there is no longer a local 'package' for `importlib` to use.

    Therefore, write the value to an asset hardcopy file and include it with the PyInstaller bundle.
    """
    version = importlib.metadata.version(distribution_name="como_recipes")
    version_string = f"v{version}"

    version_hardcopy_file_path = pathlib.Path(__file__).parent / "_assets" / "version.txt"
    with version_hardcopy_file_path.open(mode="w") as io:
        io.write(version_string)


def get_package_version() -> str:
    """Load the version hardcopy file."""
    # Must determine if path to asset is relative (in dev mode) or frozen (in production mode)
    is_bundled = hasattr(sys, "_MEIPASS")
    if is_bundled is True:
        base_path = pathlib.Path(sys._MEIPASS)  # noqa: SLF001

        version_hardcopy_file_path = base_path / "_assets" / "version.txt"
        with version_hardcopy_file_path.open(mode="r") as io:
            version_string = io.read().strip()
    else:
        save_version_hardcopy()

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


def get_terminal_size() -> tuple[int, int]:
    """Superior to the shutil.get_terminal_size() function for Windows; responds to dynamic window reshaping."""
    standard_handle = ctypes.windll.kernel32.GetStdHandle(-12)
    string_buffer = ctypes.create_string_buffer(22)
    info = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(standard_handle, string_buffer)
    if info:
        (bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy) = struct.unpack(
            "hhhhHhhhhhh",
            string_buffer.raw,
        )
        sizex = right - left + 1
        sizey = bottom - top + 1

        return sizex, sizey
    return 80, 25  # default value
