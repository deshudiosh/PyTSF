# -*- mode: python -*-
import PyInstaller.config
PyInstaller.config.CONF['distpath'] = "."

block_cipher = None


# TRY DOT NOTATION
added_files = [  
#	('C:/Python35/Lib/site-packages/remi/res/style.css', './res/style.css') 
	]

binary_files = [
		('./chromedriver.exe', '.')
	]
	

a = Analysis(['pytsf.py'],
             pathex=[''],
             binaries=binary_files,
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='PyTSF',
          debug=False,
          strip=False,
          upx=True,
          console=True )
