import os
import subprocess
import traceback
import threading
import time

from config import config
from utils import console, styledprint

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

    styledprint.styled_print(
        'Termos aceitos com sucesso',
        color=styledprint.Color.GREEN
    )
    styledprint.styled_print(
        'Iniciando servidor Minecraft...',
        color=styledprint.Color.BLUE
    )

    def start_server():
        subprocess.call(command_start, creationflags=subprocess.CREATE_NEW_CONSOLE)

    threading.Thread(target=start_server).start()

    time.sleep(3)
