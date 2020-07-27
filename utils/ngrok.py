import os
import subprocess
import threading

from subprocess import Popen, PIPE
from config import config

ngrok_path = config['path']['ngrok']


def ngrok():
    os.system(ngrok_path)


def tcp(port: int):
    command = f"ngrok tcp {port}"

    def target():
        subprocess.call(command.split(), creationflags=subprocess.CREATE_NEW_CONSOLE)

    threading.Thread(target=target()).start()
