import como_recipes


def test_simple_meal_equality():
    test_recipe_names = ["Aglio E Olio", "Brownies"]

    meal_1 = como_recipes.Meal()
    for recipe_name in test_recipe_names:
        meal_1.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name))

    meal_2 = como_recipes.Meal()
    for recipe_name in test_recipe_names:
        meal_2.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name))

    assert meal_1 == meal_2


def test_simple_meal_inequality():
    test_recipe_names_1 = ["Aglio E Olio", "Brownies"]
    test_recipe_names_2 = ["Aglio E Olio", "Carnitas"]

    meal_1 = como_recipes.Meal()
    for recipe_name in test_recipe_names_1:
        meal_1.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name))

    meal_2 = como_recipes.Meal()
    for recipe_name in test_recipe_names_2:
        meal_2.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name))

    assert meal_1 != meal_2


def test_meal_equality_with_quantity_multipliers():
    test_recipe_names = ["Aglio E Olio", "Brownies"]

    meal_1 = como_recipes.Meal(quantity_multiplier=2)
    for recipe_name in test_recipe_names:
        meal_1.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name))

    meal_2 = como_recipes.Meal(quantity_multiplier=2)
    for recipe_name in test_recipe_names:
        meal_2.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name))

    assert meal_1 == meal_2


def test_meal_inequality_with_quantity_multipliers():
    test_recipe_names = ["Aglio E Olio", "Brownies"]

    meal_1 = como_recipes.Meal(quantity_multiplier=2)
    for recipe_name in test_recipe_names:
        meal_1.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name))

    meal_2 = como_recipes.Meal(quantity_multiplier=3)
    for recipe_name in test_recipe_names:
        meal_2.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name))

    assert meal_1 != meal_2


def test_meal_add_recipe_and_len():
    meal = como_recipes.Meal()
    assert len(meal) == 0

    recipe_1 = como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio")
    meal.add_recipe(recipe=recipe_1)
    assert len(meal) == 1

    recipe_2 = como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans")
    meal.add_recipe(recipe=recipe_2)
    assert len(meal) == 2

    assert meal._recipe_name_to_recipe == {recipe_1.name: recipe_1, recipe_2.name: recipe_2}


def test_meal_remove_recipe():
    meal = como_recipes.Meal()
    assert len(meal) == 0

    meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    assert len(meal) == 1

    meal.remove_recipe(recipe_name="Aglio E Olio")
    assert len(meal) == 0


def test_meal_repr():
    meal = como_recipes.Meal()
    for recipe_name in ["Aglio E Olio", "Sauteed Green Beans"]:
        meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name))

    expected_repr = (
        "como_recipes.Meal(\n"
        "\trecipes={\n"
        '\t\tcomo_recipes.Recipe(name="Aglio E Olio", ...),\n'
        '\t\tcomo_recipes.Recipe(name="Sauteed Green Beans", ...),\n'
        "\t}\n"
        ")\n"
    )
    assert repr(meal) == expected_repr


def test_meal_str():
    meal = como_recipes.Meal()
    for recipe_name in ["Aglio E Olio", "Sauteed Green Beans"]:
        meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name))

    expected_str = "Recipes\n-------\nAglio E Olio\nSauteed Green Beans\n"
    assert str(meal) == expected_str


def test_meal_repr_with_quantity_multiplier():
    meal = como_recipes.Meal(quantity_multiplier=2)
    for recipe_name in ["Aglio E Olio", "Sauteed Green Beans"]:
        meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name))

    expected_repr = (
        "como_recipes.Meal(\n"
        "\trecipes={\n"
        '\t\tcomo_recipes.Recipe(name="Aglio E Olio", ...),\n'
        '\t\tcomo_recipes.Recipe(name="Sauteed Green Beans", ...),\n'
        "\t},\n"
        "\tquantity_multiplier=2,\n"
        ")\n"
    )
    assert repr(meal) == expected_repr


def test_meal_str_with_quantity_multiplier():
    meal = como_recipes.Meal(quantity_multiplier=2)
    for recipe_name in ["Aglio E Olio", "Sauteed Green Beans"]:
        meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name))

    expected_str = "Recipes\n-------\nAglio E Olio x2\nSauteed Green Beans x2\n"
    assert str(meal) == expected_str
