from como_recipes import Ingredient
import pytest


def test_example_ingredient_1_get_number_of_packages(example_ingredient: Ingredient):
    test_number_of_containers = example_ingredient.get_number_of_packages(amount_in_grams=56.78)
    assert test_number_of_containers == 5


def test_convert_amount_to_package_size_error_no_conversion(example_ingredient_no_conversion: Ingredient):
    with pytest.raises(NotImplementedError) as error_info:
        example_ingredient_no_conversion.get_number_of_packages(amount_in_grams=5.6)
    assert str(error_info.value) == "The default size or unit of packages containing this ingredient is not specified."
