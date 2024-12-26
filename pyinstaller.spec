# -*- mode: python ; coding: utf-8 -*-
import os
import pathlib

import como_recipes

datas = [
    ("src/como_recipes/_assets", "_assets"),
    ("pyproject.toml", "_assets"),
    ("license.txt", "_assets"),
    ("src/como_recipes/app/_app_state_json_schema.json", "_assets"),
]

if os.get("COMO_RECIPES_BASE_PATH", None) is None:
    message = (
        "Environment variable `COMO_RECIPES_BASE_PATH` must be set.\n\n"
        "Print it to console by calling `como_recipes_print_base_environment_variable`."
    )

    raise ValueError(message)

top_level_base_directory = pathlib.Path(os.environ["COMO_RECIPES_BASE_PATH"])
recipe_folder_path = top_level_base_directory / "src"/ "como_recipes" / "_recipes"
for recipe_file_path in recipe_folder_path.glob(pattern="*.yaml"):
    datas += [(str(recipe_file_path.relative_to(top_level_base_directory)).replace("\\", "/"), "_recipes")]

a = Analysis(
    ['src\\como_recipes\\app\\_app_launcher.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

executable_stem = como_recipes.utils.get_executable_stem()

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=executable_stem,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['src\\como_recipes\\_assets\\como_icon.ico'],
)
