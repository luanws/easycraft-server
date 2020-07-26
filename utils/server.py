import os
from config import config

server_path = config['path']['server']


def start():
    os.system(server_path)
