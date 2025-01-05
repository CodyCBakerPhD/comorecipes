from como_recipes import Ingredient, Measurement


def test_repr_with_prefix(example_ingredient: Ingredient):
    measurement = Measurement(amount=1, unit="grams", prefix="minced", ingredient=example_ingredient)

    expected_repr = (
        'Measurement(amount=1, unit="grams", prefix=minced), '
        'ingredient=Ingredient(name="Example Ingredient 1", '
        'default_grams_per_package=12.34, default_package_unit="container"))'
    )
    assert repr(measurement) == expected_repr


def test_repr_with_suffix(example_ingredient: Ingredient):
    measurement = Measurement(amount=2, unit="grams", ingredient=example_ingredient, suffix="room temperature")

    expected_repr = (
        'Measurement(amount=2, unit="grams", ingredient=Ingredient(name="Example '
        'Ingredient 1", default_grams_per_package=12.34, '
        'default_package_unit="container"), suffix=room temperature))'
    )
    assert repr(measurement) == expected_repr
