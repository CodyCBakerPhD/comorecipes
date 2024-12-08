import como_recipes


def test_imports():
    all_exposed = como_recipes.__all__

    for exposed_attribute_name in all_exposed:
        assert hasattr(como_recipes, exposed_attribute_name) is True
