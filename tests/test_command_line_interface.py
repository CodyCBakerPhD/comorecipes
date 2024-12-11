import importlib.metadata
import subprocess

import como_recipes


def test_cli_version():
    test_output = subprocess.run(
        ["como_recipes", "--version"],
        capture_output=True,
        text=True,
        check=False,
    ).stdout.strip()

    expected_version = importlib.metadata.version(distribution_name="como_recipes")
    assert test_output == f"v{expected_version}"


def test_version_hardcopy_current():
    test_version_string = como_recipes.utils.get_package_version()

    expected_version = importlib.metadata.version(distribution_name="como_recipes")
    expected_version_string = f"v{expected_version}"
    assert test_version_string == expected_version_string
