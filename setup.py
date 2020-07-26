import os
import shutil
import PyInstaller.__main__

PyInstaller.__main__.run([
    os.path.join('main.py'),
    '--name=%s' % 'Minecraft server',
    '--icon=%s' % os.path.join('assets', 'img', 'icon.ico'),
    '--onefile',
])

shutil.rmtree('build')
