"""Package setup."""
from setuptools import setup, find_packages
from pathlib import Path

root = Path(__file__).parent
with open(root / "README.md") as f:
    long_description = f.read()
    
with open(root / "requirements.txt") as file:
    install_requires = file.readlines()

setup(
    name="como_recipes",
    version="0.1.0",
    description="Collection of recipes and meal planning software for our household.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Cody and Molly.",
    url="https://github.com/CodyCBakerPhD/como-recipes",
    packages=find_packages(where="como_recipes"),
    package_dir={"": "como_recipes"},
    include_package_data=True,  # Includes files described in MANIFEST.in in the installation.
    python_requires=">=3.9",
    install_requires=install_requires,
)
