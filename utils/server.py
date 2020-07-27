import os
import subprocess
import traceback
import threading

from config import config

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


def start(create_new_console=False):
    command_start = f"java -Xmx1024M -Xms1024M -jar {server_path} nogui"
    if create_new_console:
        threading.Thread(
            target=lambda: subprocess.call(
                command_start,
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        ).start()
    else:
        os.system(command_start)
