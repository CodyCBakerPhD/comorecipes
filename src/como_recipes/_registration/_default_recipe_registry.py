import hashlib
import pathlib

import yaml

from ._recipe_registry import RecipeRegistry
from .._base._base_recipe import Recipe
from ..utils import request_content


class _DefaultRecipeRegistry(RecipeRegistry):
    def __init__(self) -> None:
        super().__init__()

        self._app_home_directory = pathlib.Path.home() / ".como_recipes"
        self._app_home_directory.mkdir(exist_ok=True)
        recipes_directory = self._app_home_directory / "recipes"
        recipes_directory.mkdir(exist_ok=True)
        ingredients_directory = self._app_home_directory / "ingredients"
        ingredients_directory.mkdir(exist_ok=True)
        self._manifests_directory = self._app_home_directory / "manifests"
        self._manifests_directory.mkdir(exist_ok=True)

        self._manifest_types = ["ingredient", "recipe"]
        self._current_manifest_hashes = {}
        for manifest_type in self._manifest_types:
            url = f"https://codycbakerphd.github.io/como_recipes/{manifest_type}_manifest_hash.txt"
            self._current_manifest_hashes[manifest_type] = request_content(url=url)

        update = False
        local_manifest_hash_file_paths = list(self._manifests_directory.glob(pattern="*.txt"))
        if len(local_manifest_hash_file_paths) == 0:
            update = True

        local_manifest_hashes = {}
        for manifest_hash_file_path in local_manifest_hash_file_paths:
            local_manifest_hashes[manifest_hash_file_path.stem.split("_")[0]] = manifest_hash_file_path.read_text()

        local_keys = set(local_manifest_hashes.keys())
        current_keys = set(self._current_manifest_hashes.keys())
        local_only_manifest_keys = local_keys - current_keys
        if len(local_only_manifest_keys):
            message = (
                f"\nMismatch detected between local and remote manifest files: {local_only_manifest_keys}\n\n"
                "Please manually correct these files and try again."
            )
            raise ValueError(message)

        if local_keys != current_keys:
            update = True
        else:
            for manifest_type, current_manifest_hash in self._current_manifest_hashes.items():
                local_manifest_hash = local_manifest_hashes[manifest_type]
                if local_manifest_hash == current_manifest_hash:
                    continue

                update = True

        if update is True:
            for manifest_type in self._manifest_types:
                manifest_url = f"https://codycbakerphd.github.io/como_recipes/{manifest_type}_manifest.yaml"
                manifest_content = request_content(url=manifest_url)
                manifest = yaml.safe_load(stream=manifest_content)

                for item_name, item_hash in manifest.items():
                    item_file_path = self._app_home_directory / f"{manifest_type}s" / f"{item_name}.yaml"

                    # TODO: could be more efficient to calculate the difference between local and remote manifest
                    if item_file_path.exists():
                        local_hash = hashlib.md5(string=item_file_path.read_bytes()).hexdigest()  # noqa: S324

                        if local_hash == item_hash:
                            continue

                    # TODO: could also be more efficient to make this step async
                    item_url = f"https://codycbakerphd.github.io/como_recipes/{manifest_type}s/{item_name}.yaml"
                    item_content = request_content(url=item_url)
                    item_file_path.write_text(data=item_content)

                manifest_file_path = self._manifests_directory / f"{manifest_type}s.yaml"
                manifest_file_path.write_text(data=manifest_content)

                manifest_hash_file_path = self._manifests_directory / f"{manifest_type}_hash.txt"
                manifest_hash_file_path.write_text(data=self._current_manifest_hashes[manifest_type])

        home_directory = pathlib.Path.home() / ".como_recipes"
        recipes_directory = home_directory / "recipes"
        recipe_file_paths = list(recipes_directory.glob(pattern="*.yaml"))
        recipes = {
            file_path.open().readline()[6:-1]: Recipe.from_yaml_file(file_path=file_path)
            for file_path in recipe_file_paths
        }
        self._recipes = recipes


# Initialize the global default recipe registry
default_recipe_registry = _DefaultRecipeRegistry()
