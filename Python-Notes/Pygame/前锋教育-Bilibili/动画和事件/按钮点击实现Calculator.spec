# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['按钮点击实现Calculator.py'],
             pathex=['F:\\Coding-Thomas\\Coding-Notes\\Python-Notes\\Pygame\\前锋教育-Bilibili\\动画和事件'],
             binaries=[],
             datas=[],
             hiddenimports=["pygame"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='按钮点击实现Calculator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
