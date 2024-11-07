import pathlib

from io import StringIO
from unittest.mock import patch
from como_recipes import Measurement, MeasurementRegistry, Recipe


def test_measurement_registry(example_measurement: Measurement):
    example_folder_path = pathlib.Path(__file__).parent / "examples" / "example_1"

    example_1_markdown_file_path = example_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    new_registry = MeasurementRegistry()

    assert len(new_registry) == 0
    assert repr(new_registry) == "0 registered measurements\n"
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == "0 registered measurements\n\n"

    new_registry.add_measurement(measurement=example_measurement)

    expected_repr = "1 registered measurements\n-------------------------\n\nExample Ingredient 1\n  5.6 grams\n"
    assert len(new_registry) == 1
    assert repr(new_registry) == expected_repr
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == expected_repr + "\n"

    new_registry.add_recipe(recipe=recipe)

    expected_repr = (
        "3 registered measurements\n"
        "-------------------------\n"
        "\n"
        "Example Ingredient 1\n"
        "  5.6 grams\n"
        "ingredient 1\n"
        "  3.0 tbsp.\n"
        "ingredient 2\n"
        "  4.0 g\n"
    )
    assert len(new_registry) == 3
    assert repr(new_registry) == expected_repr
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == expected_repr + "\n"


def test_get_measurement_default():
    measurement = MeasurementRegistry.get_measurement(amount=3.0, unit="grams", name="Garlic")
    assert str(type(measurement.ingredient)) == "<class 'como_recipes._ingredients._garlic.Garlic'>"
    assert measurement.ingredient.name == "Garlic"


def test_get_measurement_non_default():
    measurement = MeasurementRegistry.get_measurement(amount=3.0, unit="grams", name="Unregistered")
    assert str(type(measurement.ingredient)) == "<class 'como_recipes._base_ingredient.Ingredient'>"
    assert measurement.ingredient.name == "Unregistered"
