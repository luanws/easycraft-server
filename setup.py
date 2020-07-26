import os
import shutil
import PyInstaller.__main__
from contextlib import suppress

application_name = 'Minecraft server'
icon_path = os.path.join('assets', 'img', 'icon.ico')
ngrok_path = os.path.join('assets', 'ngrok.exe')

dist_folder_path = os.path.join('dist')

PyInstaller.__main__.run([
    os.path.join('main.py'),
    f'--name={application_name}',
    f'--icon={icon_path}',
    '--onefile',
])

shutil.rmtree('build')
os.remove(f'{application_name}.spec')

with suppress(OSError):
    shutil.copy(icon_path, dist_folder_path)
shutil.copy(ngrok_path, dist_folder_path)
