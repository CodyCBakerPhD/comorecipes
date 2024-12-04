"""
Including these directly within the top-level `__init__.py` makes them visible to autocompletion.

But we only want the imports to trigger, not for them to actually be exposed.
"""

# Only takes one import to trigger all
from ._ingredients import Garlic
from ._recipes._pydantic import AglioEOlio
from .app import CoMoApp

_hide = True
