import natsort
import pydantic

from .._base._base_recipe import Recipe


@pydantic.validate_call
def get_recipe_names_by_type(*, recipes: list[Recipe] | tuple[Recipe]) -> list[str]:
    """
    Common logic used by both `__repr__` and `__str__`.

    Fetch the recipe names in a deterministic order given alphabetically by tags (Entree vs. Side).
    """
    entrees = natsort.natsorted(seq=(recipe.name for recipe in recipes if "Entree" in recipe.tags))
    sides = natsort.natsorted(seq=(recipe.name for recipe in recipes if "Side" in recipe.tags))
    others = natsort.natsorted(seq=({recipe.name for recipe in recipes} - set(entrees) - set(sides)))
    recipe_names_by_type = entrees + sides + others

    return recipe_names_by_type
