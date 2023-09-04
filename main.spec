# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=['D:\\Uczelnia\\semestr6\\Praktyki\\infostealer\\my_infostealer\\Lib\\site-packages'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['altgraph', 'colorama', 'charset-normalizer', 'idna', 'zope.interface', 'importlib-metadata', 'install', 'Jinja2', 'MarkupSafe', 'protobuf', 'pyasn1-module', 'pytz', 'Werkzeug', 'urllib3', 'zip', 'certifi', 'google-auth-httplib2', 'googleapis-common-protos', 'google-auth', 'google-api-core', 'google-api-python-client', 'pyinstaller', 'setuptools', 'requests', 'pycryptodome', 'pip', 'Flask', 'DateTime'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
