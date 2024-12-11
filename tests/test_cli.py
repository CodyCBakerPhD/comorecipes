import importlib.metadata
import subprocess


def test_cli_version():
    test_output = subprocess.run(
        ["como_recipes", "--version"],
        capture_output=True,
        text=True,
        check=False,
    ).stdout.strip()

    expected_version = importlib.metadata.version(distribution_name="como_recipes")
    assert test_output == f"v{expected_version}"
