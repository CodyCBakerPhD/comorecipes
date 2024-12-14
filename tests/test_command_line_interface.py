import importlib.metadata
import platform
import subprocess

import como_recipes


def test_command_line_version():
    test_output = subprocess.run(
        args=["como_recipes_version"],
        capture_output=True,
        text=True,
        check=False,
    ).stdout.strip()

    expected_version = importlib.metadata.version(distribution_name="como_recipes")
    assert test_output == f"v{expected_version}"


def test_command_line_executable_name():
    """A bit of a tautological test, but still grants coverage."""
    test_executable_stem = subprocess.run(
        args=["como_recipes_executable_stem"],
        capture_output=True,
        text=True,
        check=False,
    ).stdout.strip()

    platform_name = "_".join(platform.platform().split("-")[:2])
    package_version = como_recipes.utils.get_package_version()
    expected_executable_name = f"como_recipes_{platform_name}_{package_version}"
    assert test_executable_stem == expected_executable_name

    assert "Server" not in test_executable_stem
