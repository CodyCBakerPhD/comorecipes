"""Package setup."""
from setuptools import setup, find_packages

setup(
    name="como_recipes",
    version="0.1.0",
    description="Collection of recipes and meal planning software for our household..",
    long_description_content_type="text/markdown",
    author="Cody and Molly.",
    author_email="codycbakerphd@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/CodyCBakerPhD/como-recipes",
    install_requires=["natsort", "jsonschema"],
)
