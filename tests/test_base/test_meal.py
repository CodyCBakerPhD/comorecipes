import como_recipes


def test_simple_meal_equality():
    test_recipe_names = ["Aglio E Olio", "Brownies"]

    meal_1 = como_recipes.Meal(
        recipes={
            como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name)
            for recipe_name in test_recipe_names
        },
    )
    meal_2 = como_recipes.Meal(
        recipes={
            como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name)
            for recipe_name in test_recipe_names
        },
    )
    assert meal_1 == meal_2


def test_simple_meal_inequality():
    test_recipe_names_1 = ["Aglio E Olio", "Brownies"]
    test_recipe_names_2 = ["Aglio E Olio", "Carnitas"]

    meal_1 = como_recipes.Meal(
        recipes={
            como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name)
            for recipe_name in test_recipe_names_1
        },
    )
    meal_2 = como_recipes.Meal(
        recipes={
            como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name)
            for recipe_name in test_recipe_names_2
        },
    )
    assert meal_1 != meal_2


def test_meal_equality_with_quantity_multipliers():
    test_recipe_names = ["Aglio E Olio", "Brownies"]

    meal_1 = como_recipes.Meal(
        recipes={
            como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name)
            for recipe_name in test_recipe_names
        },
        quantity_multiplier=2,
    )
    meal_2 = como_recipes.Meal(
        recipes={
            como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name)
            for recipe_name in test_recipe_names
        },
        quantity_multiplier=2,
    )
    assert meal_1 == meal_2


def test_meal_inequality_with_quantity_multipliers():
    test_recipe_names = ["Aglio E Olio", "Brownies"]

    meal_1 = como_recipes.Meal(
        recipes={
            como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name)
            for recipe_name in test_recipe_names
        },
        quantity_multiplier=2,
    )
    meal_2 = como_recipes.Meal(
        recipes={
            como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name)
            for recipe_name in test_recipe_names
        },
        quantity_multiplier=3,
    )
    assert meal_1 != meal_2


def test_meal_add_recipe():
    meal = como_recipes.Meal(recipes={como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio")})
    meal.add_default_recipe(recipe_name="Sauteed Green Beans")

    assert len(meal.recipes) == 2
    assert {"Aglio E Olio", "Sauteed Green Beans"} == {recipe.name for recipe in meal.recipes}


def test_meal_remove_recipe():
    meal = como_recipes.Meal(recipes={como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio")})
    meal.remove_default_recipe(recipe_name="Aglio E Olio")

    assert len(meal.recipes) == 0


def test_example_meals_inequality(example_meal_1: como_recipes.Meal, example_meal_2: como_recipes.Meal):
    """Unequal due to the different quantity multipliers."""
    assert example_meal_1 != example_meal_2


def test_example_meal_1_repr(example_meal_1: como_recipes.Meal):
    expected_repr = (
        "como_recipes.Meal(\n"
        "\trecipes={\n"
        '\t\tcomo_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E '
        'Olio"),\n'
        '\t\tcomo_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed '
        'Green Beans"),\n'
        "\t}\n"
        ")\n"
    )
    assert repr(example_meal_1) == expected_repr


def test_example_meal_1_str(example_meal_1: como_recipes.Meal):
    expected_str = "Recipes\n-------\nAglio E Olio\nSauteed Green Beans\n"
    assert str(example_meal_1) == expected_str


def test_example_meal_2_repr(example_meal_2: como_recipes.Meal):
    expected_repr = (
        "como_recipes.Meal(\n"
        "\trecipes={\n"
        '\t\tcomo_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E '
        'Olio"),\n'
        '\t\tcomo_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed '
        'Green Beans"),\n'
        "\t},\n"
        "\tquantity_multiplier=2,\n"
        ")\n"
    )
    assert repr(example_meal_2) == expected_repr


def test_example_meal_2_str(example_meal_2: como_recipes.Meal):
    expected_str = "Recipes\n-------\nAglio E Olio x2\nSauteed Green Beans x2\n"
    assert str(example_meal_2) == expected_str
