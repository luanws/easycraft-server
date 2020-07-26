import os
from config import config

ngrok_path = config['path']['ngrok']


def ngrok():
    os.system(ngrok_path)


