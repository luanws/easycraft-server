import os
import subprocess
from config import config

server_path = config['path']['server']


def accept_terms():
    if os.path.isfile('eula.txt'):
        with open('eula.txt') as f:
            eula = f.read()
        with open('eula.txt', 'w') as f:
            accept_eula = eula.replace('eula=false', 'eula=true')
            f.write(accept_eula)


def start():
    accept_terms()
    os.system(f"java -Xmx1024M -Xms1024M -jar {server_path} nogui")
