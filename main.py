import os
import subprocess
from utils import styledprint
from config import config

ngrok_path = 'assets\\ngrok'

styledprint.styled_print(config['application_name'].upper(), color=styledprint.Color.GREEN)
subprocess.call(ngrok_path, creationflags=subprocess.CREATE_NEW_CONSOLE)
input()
