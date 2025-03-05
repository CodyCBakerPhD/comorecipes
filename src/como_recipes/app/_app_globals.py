import json
import pathlib

import natsort

from .._registration._default_recipe_registry import default_recipe_registry
from ..utils import get_bundle_base_path, is_bundled

recipe_types = ("Entree", "Side", "Dessert")
exclusive_availability_recipe_types = ("Entree", "Dessert")

cuisines = (
    "American",
    "Asian",
    "Brazilian",
    "British",
    "European",
    "French",
    "Greek",
    "Italian",
    "Jamaican",
    "Mexican",
)

all_default_tags: tuple[str] = tuple(
    natsort.natsorted(
        seq={
            tag
            for recipe_name in default_recipe_registry.get_all_recipe_names()
            for tag in default_recipe_registry.get_recipe(recipe_name=recipe_name).tags
        },
    ),
)

default_index_to_recipe_name: dict[int, str] = {
    index: recipe_name
    for index, recipe_name in enumerate(
        natsort.natsorted(seq=default_recipe_registry.get_all_recipe_names()),
    )
}

# TODO: can this be removed?
default_recipe_name_to_index: dict[str, int] = {
    recipe_name: index for index, recipe_name in default_index_to_recipe_name.items()
}

default_recipe_name_to_type: dict[str, tuple[str, ...]] = {
    recipe_name: tuple(
        recipe_type
        for recipe_type in recipe_types
        if recipe_type in default_recipe_registry.get_recipe(recipe_name=recipe_name).tags
    )
    for recipe_name in default_recipe_registry.get_all_recipe_names()
}

if is_bundled() is True:
    bundle_path = get_bundle_base_path()
    _app_state_json_schema_file_path = bundle_path / "_assets" / "_app_state_json_schema.json"
else:
    _app_state_json_schema_file_path = pathlib.Path(__file__).parent / "_app_state_json_schema.json"
with _app_state_json_schema_file_path.open("r") as io:
    app_state_json_schema = json.load(fp=io)
