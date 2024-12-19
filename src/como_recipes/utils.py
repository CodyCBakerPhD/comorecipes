"""Collection of minor help functions."""

import importlib.metadata
import pathlib
import platform
import sys

import natsort
import pydantic

from ._base._base_recipe import Recipe


def is_bundled() -> bool:
    """Determine if the application is bundled by PyInstaller."""
    result = hasattr(sys, "_MEIPASS")

    return result


def get_bundle_path() -> pathlib.Path:
    """Determine the bundled (temporary PyInstaller) path for the application."""
    if is_bundled() is False:
        message = "Application is not bundled."

        raise RuntimeError(message)

    bundle_path = pathlib.Path(sys._MEIPASS)  # noqa: SLF001

    return bundle_path


def get_license_text() -> str:
    """Load the license text file."""
    if is_bundled() is True:
        bundle_path = get_bundle_path()

        file_path = bundle_path / "_assets" / "license.txt"  # Is copied to _assets during build
        with file_path.open(mode="r") as io:
            license_text = io.read()
    else:
        file_path = pathlib.Path(__file__).parent.parent.parent / "license.txt"
        with file_path.open(mode="r") as io:
            license_text = io.read()

    return license_text


def get_package_version() -> str:
    """Load the version directly from the TOML file."""
    if is_bundled() is True:
        bundle_path = get_bundle_path()

        file_path = bundle_path / "_assets" / "pyproject.toml"  # Is copied to _assets during build
        with file_path.open(mode="r") as io:
            lines = io.readlines()

        version_line = next(line for line in lines if "version" in line)
        version = version_line.split("=")[1].strip().strip('"')
    else:
        version = importlib.metadata.version(distribution_name="como_recipes")
    version_string = f"v{version}"

    return version_string


def get_executable_stem() -> str:
    """
    Determine the executable name for the application.

    Only supports Windows patterns for the time being.
    """
    platform_name = "_".join(platform.platform().split("-")[:2])

    # Resolve an issue with GitHub Actions builds
    corrected_platform_name = platform_name.removesuffix("Server")

    # Improve readability for users when built by GitHub Actions
    match corrected_platform_name:
        case "Windows_2019":
            improved_platform_name = "Windows_10"
        case "Windows_2022":
            improved_platform_name = "Windows_11"
        case _:
            improved_platform_name = corrected_platform_name

    package_version = get_package_version()
    executable_stem = f"como_recipes_{improved_platform_name}_{package_version}"

    return executable_stem


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
