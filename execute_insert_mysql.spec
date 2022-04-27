# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['execute_insert_mysql.py'],
    pathex=['C:\\Users\\AZKA\\Documents\\koding2an_baru\\DWH\\DWH'],
    binaries=[],
    datas=[('C:\\Users\\AZKA\\Documents\\koding2an_baru\\DWH\\DWH\\configuration.csv', '.'),
    ('C:\\Users\\AZKA\\Documents\\koding2an_baru\\DWH\\DWH\\dwh_log.log','.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='execute_insert_mysql',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='execute_insert_mysql',
)
