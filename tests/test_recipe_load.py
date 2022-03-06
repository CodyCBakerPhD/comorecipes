from unittest import TestCase
from pathlib import Path

from como_recipes import load_recipe, Recipe


class TestRecipeLoad(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.recipe_paths = Path(__file__).parent.parent / "como_recipes"

    def test_recipe_load(self):
        pass
