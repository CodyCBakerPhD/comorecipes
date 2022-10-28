"""Test recipe loading."""
from pathlib import Path
from unittest import TestCase


class TestRecipeLoad(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.recipe_paths = Path(__file__).parent.parent / "como_recipes"
