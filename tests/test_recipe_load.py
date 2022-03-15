import jsonschema
import json
from unittest import TestCase
from pathlib import Path
from jsonschema import ValidationError

from como_recipes import load_recipe


class TestRecipeLoad(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.recipe_paths = Path(__file__).parent.parent / "como_recipes"

        with open(file=Path(__file__).parent.parent / "recipe_schema.json", mode="r") as fp:
            cls.recipe_schema = json.load(fp=fp)

    def test_recipe_load(self):
        for file_path in (Path(__file__).parent.parent / "como_recipes" / "recipes").iterdir():
            if ".md" in file_path.suffixes:
                recipe = load_recipe(file_path=file_path)
                recipe.ingredients = [x.__dict__ for x in recipe.ingredients]  # for schema validation
                recipe.instructions = ""
                jsonschema.validate(instance=recipe.__dict__, schema=self.recipe_schema)

    def test_schema_bad_recipe(self):
        with self.assertRaises(expected_exception=ValidationError):
            jsonschema.validate(instance=dict(WRONG=dict()), schema=self.recipe_schema)

    def test_schema_bad_ingredient(self):
        with self.assertRaises(expected_exception=ValidationError):
            jsonschema.validate(instance=dict(name="test", ingredients=[dict(WRONG=1)]), schema=self.recipe_schema)
