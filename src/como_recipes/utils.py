"""Collection of minor help functions."""

import ctypes
import struct

import natsort

from ._base._base_recipe import Recipe


def get_recipe_names_by_type(recipes: list[Recipe] | set[Recipe]) -> list[str]:
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
