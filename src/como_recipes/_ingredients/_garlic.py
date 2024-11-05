from .._base_ingredient import Ingredient
from .._ingredient_registration import default_ingredient_registry


class Garlic(Ingredient):
    name: str = "garlic"
    grams_to_default_package_conversion: float = 1.0
    default_package_unit: str = "head"


default_ingredient_registry.add_ingredient(ingredient=Garlic())
