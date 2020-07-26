import os
import traceback
import subprocess
from config import config
from utils import console

server_path = config['path']['server']


def accept_terms() -> bool:
    try:
        with open('eula.txt') as f:
            eula = f.read()
        with open('eula.txt', 'w') as f:
            accept_eula = eula.replace('eula=false', 'eula=true')
            f.write(accept_eula)
        return True
    except FileNotFoundError:
        return False
    except Exception:
        traceback.print_exc()
        return False


def start():
    command_start = f"java -Xmx1024M -Xms1024M -jar {server_path} nogui"
    while not accept_terms():
        os.system(command_start)
        console.clear()

    subprocess.call(command_start)
