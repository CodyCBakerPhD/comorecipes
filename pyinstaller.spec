# -*- mode: python ; coding: utf-8 -*-
import platform
import como_recipes

a = Analysis(
    ['src\\como_recipes\\app\\_app_launcher.py'],
    pathex=[],
    binaries=[],
    datas=[('src/como_recipes/_assets', '_assets'), ('pyproject.toml', '_assets'), ('license.txt', '_assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

# Only supports Windows for now
platform_name = "_".join(platform.platform().split("-")[:2])
package_version = como_recipes.utils.get_package_version()
app_name = f"como_recipes_{platform_name}_{package_version}"

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=app_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['src\\como_recipes\\_assets\\como_icon.ico'],
)
