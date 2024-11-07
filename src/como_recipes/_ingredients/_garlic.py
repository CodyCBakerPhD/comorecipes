from .._base_ingredient import Ingredient
from .._ingredient_registration import default_ingredient_registry


class Garlic(Ingredient):
    name: str = "garlic"
    default_grams_per_package: int | float | None = 1.0
    default_package_unit: str | None = "head"


default_ingredient_registry.add_ingredient(ingredient=Garlic())
