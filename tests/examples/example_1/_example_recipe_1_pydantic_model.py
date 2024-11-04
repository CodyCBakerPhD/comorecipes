from como_recipes import Recipe, MeasuredIngredient


class ExampleRecipe1PydanticModel(Recipe):
    name = "Example Recipe 1"
    ingredients = [
        MeasuredIngredient(name="ingredient 1", amount=3, unit="tbsp."),
        MeasuredIngredient(name="ingredient 2", amount=4, unit="g"),
    ]
    instructions = [
        "This is an example of a recipe.",
    ]
