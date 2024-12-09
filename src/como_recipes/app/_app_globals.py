import natsort

from .._registration._recipe_registry import default_recipe_registry

all_default_tags = natsort.natsorted(
    seq={
        tag
        for recipe_name in default_recipe_registry.get_all_recipe_names()
        for tag in default_recipe_registry.get_recipe(recipe_name=recipe_name).tags
    },
)
