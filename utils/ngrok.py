import os
import subprocess
import threading
from typing import Optional
import webbrowser
from contextlib import suppress
from config import config

ngrok_path = config['path']['ngrok']


def get_saved_auth_token() -> Optional[str]:
    with suppress(FileNotFoundError):
        with open(config['path']['ngrok_auth_token']) as f:
            return f.read()
    return None


def save_auth_token(auth_token: str) -> Optional[str]:
    with open(config['path']['ngrok_auth_token'], 'w') as f:
        f.write(auth_token)


def request_auth_token() -> str:
    webbrowser.open(config['url']['ngrok_login'])
    print('Faça login no site do ngrok e copie o authtoken')
    auth_token = input('Authtoken: ')
    return auth_token


def login(auth_token: str) -> str:
    os.system(f"{ngrok_path} authtoken {auth_token}")


def ngrok():
    os.system(ngrok_path)


def tcp(port: int):
    command = f"{ngrok_path} tcp {port}"

    def target():
        auth_token = get_saved_auth_token()
        if auth_token is None:
            auth_token = request_auth_token()
            save_auth_token(auth_token)
        login(auth_token)
        subprocess.call(
            command.split(),
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )

    threading.Thread(target=target()).start()
