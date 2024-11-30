import io
import pathlib
import re
import unittest.mock

import pytest

from como_recipes import Measurement, MeasurementRegistry, Recipe


def test_measurement_registry(example_measurement: Measurement):
    example_folder_path = pathlib.Path(__file__).parent / "examples" / "example_1"

    example_1_markdown_file_path = example_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    new_registry = MeasurementRegistry()

    assert len(new_registry) == 0
    assert repr(new_registry) == "0 registered measurements\n"
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == "0 registered measurements\n\n"

    new_registry.add_measurement(measurement=example_measurement)

    expected_repr = "1 registered measurements\n-------------------------\n\nExample Ingredient 1\n  56 grams\n"
    assert len(new_registry) == 1
    assert repr(new_registry) == expected_repr
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == expected_repr + "\n"

    expected_shopping_list = "Example Ingredient 1\n  56 grams\n"
    assert new_registry.get_shopping_list() == expected_shopping_list

    new_registry.add_recipe(recipe=recipe)

    expected_repr = (
        "3 registered measurements\n"
        "-------------------------\n"
        "\n"
        "Example Ingredient 1\n"
        "  56 grams\n"
        "ingredient 1\n"
        "  31/10 tbsp.\n"
        "ingredient 2\n"
        "  4 g\n"
    )
    assert len(new_registry) == 3
    assert repr(new_registry) == expected_repr
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == expected_repr + "\n"

    new_registry.add_measurement(measurement=example_measurement)

    expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\ningredient 2\n  4 g\n"
    assert new_registry.get_shopping_list() == expected_shopping_list

    new_registry.remove_measurement(
        measurement=MeasurementRegistry.get_measurement(amount=2.0, unit="g", name="ingredient 2"),
    )

    expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\ningredient 2\n  2 g\n"
    assert new_registry.get_shopping_list() == expected_shopping_list

    # Recipe should now be removed entirely from printout
    new_registry.remove_measurement(
        measurement=MeasurementRegistry.get_measurement(amount=2.0, unit="g", name="ingredient 2"),
    )

    expected_shopping_list = "Example Ingredient 1\n  112 grams\ningredient 1\n  31/10 tbsp.\n"
    assert new_registry.get_shopping_list() == expected_shopping_list

    expected_recipe_names = ["Example Recipe 1"]
    assert expected_recipe_names == new_registry.get_all_recipe_names()

    new_registry.remove_recipe(recipe_name="Example Recipe 1")

    expected_shopping_list = "Example Ingredient 1\n  112 grams\n"
    assert new_registry.get_shopping_list() == expected_shopping_list


def test_get_measurement_default():
    measurement = MeasurementRegistry.get_measurement(amount=1.0, unit="grams", name="Garlic")
    assert str(type(measurement.ingredient)) == "<class 'como_recipes._ingredients._garlic.Garlic'>"
    assert measurement.ingredient.name == "Garlic"


def test_get_measurement_non_default():
    measurement = MeasurementRegistry.get_measurement(amount=1.0, unit="grams", name="Unregistered")
    assert str(type(measurement.ingredient)) == "<class 'como_recipes._base_ingredient.Ingredient'>"
    assert measurement.ingredient.name == "Unregistered"


def test_get_shopping_list_error():
    new_registry = MeasurementRegistry()

    measurement_1 = MeasurementRegistry.get_measurement(amount=1.0, unit="g", name="test_ingredient")
    new_registry.add_measurement(measurement=measurement_1)
    measurement_2 = MeasurementRegistry.get_measurement(amount=1.0, unit="tsp", name="test_ingredient")
    new_registry.add_measurement(measurement=measurement_2)

    expected_message = "\nMultiple units found for ingredient 'test_ingredient':\n\n[\n  1 g\n  1 tsp\n]"
    with pytest.raises(ValueError, match=re.escape(pattern=expected_message)):
        new_registry.get_shopping_list()


def test_get_shopping_list_warning():
    new_registry = MeasurementRegistry()

    measurement_1 = MeasurementRegistry.get_measurement(amount=1.0, unit="g", name="test_ingredient")
    new_registry.add_measurement(measurement=measurement_1)

    measurement_2 = MeasurementRegistry.get_measurement(amount=2.0, unit="g", name="test_ingredient")
    new_registry.remove_measurement(measurement=measurement_2)

    expected_message = "Negative amount of 'test_ingredient' found in shopping list; ignoring."
    with pytest.warns(UserWarning, match=expected_message):
        new_registry.get_shopping_list()
