import collections

from .._registration._default_recipe_registry import default_recipe_registry


def get_recipe_name_hierarchy(
    recipe_names: tuple[str, ...],
    recipe_types: tuple[str] = ("Entree", "Side", "Dessert"),
) -> dict[str, tuple[str, ...]]:
    """Create a recipe name hierarchy string."""
    # TODO: make LRU cached retrieval
    default_recipe_name_to_type: dict[str, tuple[str, ...]] = {
        recipe_name: tuple(
            recipe_type
            for recipe_type in recipe_types
            if recipe_type in default_recipe_registry.get_recipe(recipe_name=recipe_name).tags
        )
        for recipe_name in default_recipe_registry.get_all_recipe_names()
    }

    hierarchy = {}
    organized_recipe_names = collections.defaultdict(bool)
    for recipe_type in recipe_types:
        values = tuple(
            recipe_name
            for recipe_name in recipe_names
            if recipe_type in default_recipe_name_to_type[recipe_name]  # TODO: would a hash map be better?
            and organized_recipe_names[recipe_name] is False
        )

        if any(values) is False:
            continue

        organized_recipe_names.update({value: True for value in values})

        hierarchy[recipe_type] = values

    return hierarchy
