# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['写字板12.1.4.py'],
             pathex=['E:\\王一涵programThomas\\王一涵PythonThomas\\Python-Learned\\学习\\图形界面开发学习笔记\\《Python基础教程》系列'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          name='写字板12.1.4',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='wordpad.ico')
