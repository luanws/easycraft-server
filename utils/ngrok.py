import os
import subprocess
from config import config

ngrok_path = config['path']['ngrok']


def ngrok():
    os.system(ngrok_path)


def tcp(port: int) -> str:
    command = f"ngrok tcp {port}"
    os.system(command)
    # return subprocess.run(command, capture_output=True, text=True)
