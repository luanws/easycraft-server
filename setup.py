import os
import shutil
import PyInstaller.__main__
from contextlib import suppress
from config import config

application_name = config['application_name']
icon_path = os.path.join('assets', 'img', 'icon.ico')
ngrok_path = os.path.join('assets', 'ngrok.exe')

assets_folder_path = os.path.join('assets')
dist_folder_path = os.path.join('dist')
assets_dist_folder_path = os.path.join(dist_folder_path, 'assets')

PyInstaller.__main__.run([
    os.path.join('main.py'),
    f'--name={application_name}',
    f'--icon={icon_path}',
    '--onefile',
])

with suppress(FileNotFoundError):
    shutil.rmtree('build')
with suppress(FileNotFoundError):
    os.remove(f'{application_name}.spec')

with suppress(FileExistsError):
    os.mkdir(assets_dist_folder_path)

shutil.copy(icon_path, dist_folder_path)
shutil.copy(ngrok_path, assets_dist_folder_path)
