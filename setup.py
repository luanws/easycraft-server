import os
import shutil
import PyInstaller.__main__

application_name = 'Minecraft server'
icon_path = os.path.join('assets', 'img', 'icon.ico')

dist_folder_path = os.path.join('dist')

PyInstaller.__main__.run([
    os.path.join('main.py'),
    f'--name={application_name}',
    f'--icon={icon_path}',
    '--onefile',
])

shutil.rmtree('build')
os.remove(f'{application_name}.spec')

shutil.copy(icon_path, dist_folder_path)
