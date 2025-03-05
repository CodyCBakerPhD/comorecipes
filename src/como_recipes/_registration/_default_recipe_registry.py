import pathlib

from ._recipe_registry import RecipeRegistry
from .._base._base_recipe import Recipe
from ..utils import get_bundle_base_path, is_bundled


class _DefaultRecipeRegistry(RecipeRegistry):
    def __init__(self) -> None:
        super().__init__()

        _default_recipes_directory = (
            pathlib.Path(__file__).parent.parent.parent.parent / "docs" / "recipes"
            if is_bundled() is False
            else get_bundle_base_path() / "_recipes"
        )
        _recipes = {
            file_path.open().readline()[6:-1]: Recipe.from_yaml_file(file_path=file_path)
            for file_path in _default_recipes_directory.glob(pattern="*.yaml")
        }
        self._recipes = _recipes


# Initialize the global default recipe registry
default_recipe_registry = _DefaultRecipeRegistry()
