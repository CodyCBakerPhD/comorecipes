"""Collection of help functions."""
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Union

from pydantic import FilePath

from ._base import Recipe, MeasuredIngredient

def rational_string_to_float(string: str) -> float:
    """Small helper function to convert strings into floats ('1/4' becomes 0.25)."""
    if "/" in string:
        numerator, denominator = string.split("/")
        return int(numerator) / int(denominator)
    else:
        return float(string)

