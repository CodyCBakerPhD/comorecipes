import jsonschema
import json
from unittest import TestCase
from pathlib import Path

from como_recipes import load_recipe


class TestRecipeLoad(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.recipe_paths = Path(__file__).parent.parent / "como_recipes"

    def test_recipe_load(self):
        for file_path in (Path(__file__).parent.parent / "como_recipes" / "recipes").iterdir():
            if ".md" in file_path.suffixes:
                recipe = load_recipe(file_path=file_path)
                recipe.ingredients = [x.__dict__ for x in recipe.ingredients]  # for schema validation
                recipe.instructions = ""
                recipe = recipe.__dict__
                with open(file=Path(__file__).parent.parent / "recipe_schema.json", mode="r") as fp:
                    schema = json.load(fp=fp)
                jsonschema.validate(instance=recipe, schema=schema)
