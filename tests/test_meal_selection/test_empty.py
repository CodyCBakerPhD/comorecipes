import io
import unittest.mock

import pytest

from como_recipes import MealSelection


def test_empty_meal_selection_repr():
    meal_selection = MealSelection()

    expected_repr = "\ncomo_recipes.MealSelection()\n"
    assert repr(meal_selection) == expected_repr


def test_empty_meal_selection_print():
    meal_selection = MealSelection()

    expected_print = "\ncomo_recipes.MealSelection()\n\n"
    with unittest.mock.patch("sys.stdout", new=io.StringIO()) as captured_output:
        print(meal_selection)
    assert captured_output.getvalue() == expected_print


def test_get_raw_measurement_list_empty_error():
    meal_selection = MealSelection()

    with pytest.raises(
        expected_exception=ValueError,
        match="No meals or measurements have been added to the meal selection.",
    ):
        meal_selection.get_raw_measurement_list()


def test_empty_get_shopping_list():
    meal_selection = MealSelection()

    shopping_list = meal_selection.get_shopping_list()
    assert shopping_list == {}


def test_empty_get_shopping_list_display():
    meal_selection = MealSelection()

    shopping_list = meal_selection.get_shopping_list_display()
    assert shopping_list == []


def test_empty_get_shopping_list_printout():
    meal_selection = MealSelection()

    shopping_list = meal_selection.get_shopping_list_printout()
    assert shopping_list == ""
