# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['HEX_Chooser.pyw'],
             pathex=['E:\\ProgramThomas\\Coding-Notes\\Python-Notes\\学习\\图形界面开发学习笔记\\PythonGUI设计tkinter菜鸟编程书\\Scale'],
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
          name='HEX_Chooser',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
