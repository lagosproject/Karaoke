# -*- mode: python ; coding: utf-8 -*-
import os
import pygame

pygame_dir = os.path.dirname(pygame.__file__)
font_src = os.path.join(pygame_dir, 'freesansbold.ttf')

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[(font_src, '.')],
    hiddenimports=[
        'sounddevice',
        'soundfile',
        'numpy',
        'cffi',
        '_cffi_backend',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='karaoke',
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
)
