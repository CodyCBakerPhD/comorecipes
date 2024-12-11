import natsort

from .._registration._recipe_registry import default_recipe_registry

all_default_tags: list[str] = natsort.natsorted(
    seq={
        tag
        for recipe_name in default_recipe_registry.get_all_recipe_names()
        for tag in default_recipe_registry.get_recipe(recipe_name=recipe_name).tags
    },
)

default_index_to_recipe_name: dict[int, str] = {
    index: recipe_name
    for index, recipe_name in enumerate(
        natsort.natsorted(seq=default_recipe_registry.get_all_recipe_names()),
    )
}
default_recipe_name_to_index: dict[str, int] = {
    recipe_name: index for index, recipe_name in default_index_to_recipe_name.items()
}

default_entree_to_index: dict[int, str] = {
    recipe_name: index
    for index, recipe_name in default_index_to_recipe_name.items()
    # TODO: enable when more recipes are tagged properly
    # if "Entree" in default_recipe_registry.get_recipe(recipe_name=recipe_name).tags
}
