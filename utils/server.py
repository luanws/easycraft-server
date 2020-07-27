import re
import os
import subprocess
import traceback
import threading

from config import config

server_path = config['path']['server']
server_properties_path = os.path.join('server.properties')


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


def get_all_properties() -> str:
    with open(server_properties_path) as f:
        properties = f.read()
        return properties


def get_property(key: str) -> str:
    properties = get_all_properties()
    property = re.findall(rf'{key}=(.+)', properties)[0]
    return property


def set_property(key: str, value: str):
    properties = get_all_properties()

    new_property = f"{key}={value}"
    try:
        old_property = f"{key}={get_property(key)}"
        with open(server_properties_path, 'w') as f:
            f.write(properties.replace(old_property, new_property))
    except IndexError:
        with open(server_properties_path, 'a') as f:
            f.write(new_property)
