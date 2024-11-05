from como_recipes import Recipe, MeasuredIngredient, default_recipe_registry


class ExampleRecipe1(Recipe):
    name: str = "Example Recipe 1"
    measurements: list[MeasuredIngredient] = [
        MeasuredIngredient(name="ingredient 1", amount=3.0, unit="tbsp."),
        MeasuredIngredient(name="ingredient 2", amount=4.0, unit="g"),
    ]
    instructions: list[str] = [
        "This is an example of a recipe.",
    ]


default_recipe_registry.add_recipe(recipe=ExampleRecipe1())
