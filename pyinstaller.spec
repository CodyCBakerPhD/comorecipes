# -*- mode: python ; coding: utf-8 -*-
import como_recipes

a = Analysis(
    ['src\\como_recipes\\app\\_app_launcher.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src/como_recipes/_assets', '_assets'),
        ('pyproject.toml', '_assets'),
        ('license.txt', '_assets'),
        ('src/como_recipes/app/_app_state_json_schema.json', '_assets'),
    ],
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
