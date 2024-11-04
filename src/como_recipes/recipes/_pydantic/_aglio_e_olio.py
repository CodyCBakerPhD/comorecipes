from ..._base import Recipe, MeasuredIngredient


class AglioEOlio(Recipe):
    name: str = "Aglio E Olio"
    ingredients: list[MeasuredIngredient] = [
        # MeasuredIngredient(name="", amount=1, unit=""),
        #
        # 2 qt.water
        #
        # 1 tbsp.salt
        #
        # 1 lb.thin spaghetti
        #
        # 1 / 3 cup olive oil
        #
        # 8 large cloves of garlic
        #
        # 2 tsp.crushed red pepper
        #
        # 1 / 4 cup parsley
        #
        # 1 cup fresh Parmesan
    ]
    instructions: list[str] = [
        "Bring water and salt to boil. Cook pasta. Set aside 3/2 cup of pasta water before draining.",
        "Heat olive oil over medium heat in a large pot.",
        "Add garlic and cook for 1-2 minutes, stirring frequently until it just turns golden.",
        "Add red pepper and cook 30 seconds more.",
        "Carefully add reserved pasta water and bring to boil.",
        "Lower heat and simmer for 5 minutes, until liquid is reduced by about a third.",
        "Incorporate pasta, parsley, and Parmesan.",
    ]
