from ..._base import Recipe, MeasuredIngredient
from ..._registration import default_recipe_registry


class AglioEOlio(Recipe):
    name: str = "Aglio E Olio"
    ingredients: list[MeasuredIngredient] = [
        MeasuredIngredient(name="water", amount=2.0, unit="qt."),
        MeasuredIngredient(name="salt", amount=1.0, unit="tbsp."),
        MeasuredIngredient(name="thin spaghetti", amount=1.0, unit="lb."),
        MeasuredIngredient(name="olive oil", amount=0.3333333333333333, unit="cup"),
        MeasuredIngredient(name="cloves of garlic", amount=8.0, unit="large"),
        MeasuredIngredient(name="crushed red pepper", amount=2.0, unit="tsp."),
        MeasuredIngredient(name="parsley", amount=0.25, unit="cup"),
        MeasuredIngredient(name="fresh Parmesan", amount=1.0, unit="cup"),
    ]
    instructions: list[str] = [
        "Bring water and salt to boil. Cook pasta. Set aside 3/2 cup of pasta water before draining.",
        "Heat olive oil over medium heat in a large pot.",
        "Add garlic and cook for 1-2 minutes, stirring frequently until it just turns golden.",
        "Add red pepper and cook 30 seconds more.",
        "Carefully add reserved pasta water and bring to boil.",
        "Lower heat and simmer for 5 minutes, until liquid is reduced by about a third.",
        "Incorporate pasta, parsley, and Permesan.",
    ]


default_recipe_registry.update_registry(recipe=AglioEOlio())
