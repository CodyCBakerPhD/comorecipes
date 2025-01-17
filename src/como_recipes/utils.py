"""Collection of minor help functions."""

import importlib.metadata
import pathlib
import platform
import sys

import pydantic

from ._base._base_measurement import Measurement


def is_bundled() -> bool:
    """Determine if the application is bundled by PyInstaller."""
    result = hasattr(sys, "_MEIPASS")

    return result


def get_bundle_base_path() -> pathlib.Path:
    """Determine the bundled (temporary PyInstaller) path for the application."""
    if is_bundled() is False:
        message = "Application is not bundled."

        raise RuntimeError(message)

    bundle_path = pathlib.Path(sys._MEIPASS)  # noqa: SLF001

    return bundle_path


def get_base_environment_variable() -> str:
    """Determine the base development path for the package and set it as an environment variable."""
    if is_bundled() is True:
        message = "Application is bundled."

        raise RuntimeError(message)

    dev_path = pathlib.Path(__file__).parent.parent.parent

    return str(dev_path)


def get_license_text() -> str:
    """Load the license text file."""
    if is_bundled() is True:
        bundle_path = get_bundle_base_path()

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
        bundle_path = get_bundle_base_path()

        file_path = bundle_path / "_assets" / "pyproject.toml"  # Is copied to _assets during build
        with file_path.open(mode="r") as io:
            lines = io.readlines()

        version_line = next(line for line in lines if "version" in line)
        version = version_line.split("=")[1].strip().strip('"')
    else:
        version = importlib.metadata.version(distribution_name="como_recipes")
    version_string = f"v{version}"

    return version_string


def get_executable_name(package_version: str) -> str:
    """Determine the executable name for the main CoMo Recipes app."""
    platform_name = "_".join(platform.platform().split("-")[:2])

    # Resolve an issue with GitHub Actions builds
    corrected_platform_name = platform_name.replace("Server", "")

    # Linux doesn't add a suffix; MacOS is not supported
    platform_suffix = ".exe" if "Windows" in corrected_platform_name else ""
    executable_name = f"como_recipes_{corrected_platform_name}_{package_version}{platform_suffix}"

    return executable_name


@pydantic.validate_call
def get_rendered_units(*, measurement: Measurement) -> str:
    """
    Fancy rendering of the units for the measurement.

    Makes decisions based on value of portions and presence of other metadata.
    """
    if measurement.amount == "enough":
        return ""
    if measurement.unit == "portions" and measurement.ingredient.portions_text is not None:
        return measurement.ingredient.portions_text
    return measurement.unit
