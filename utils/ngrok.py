import os

ngrok_path = os.path.join('assets', 'ngrok')


def start():
    os.system(ngrok_path)
