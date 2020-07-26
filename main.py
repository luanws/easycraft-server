from config import config
from typing import List
from contextlib import suppress
from utils import styledprint, console

from options.download_minecraft_server import DownloadMinecraftServer
from models.option import Option

ngrok_path = 'assets\\ngrok'


def hr():
    print('--------------------------------------------------')


options: List[Option] = [
    DownloadMinecraftServer(),
]


def start():
    console.clear()
    styledprint.styled_print(
        config['application_name'].upper(),
        color=styledprint.Color.GREEN
    )

    print()
    menu_options = "\n".join([f"({i}) {option.name}" for i, option in enumerate(options, 1)])
    print(styledprint.indent(
        menu_options,
        color=styledprint.Color.BLUE
    ))

    print()
    option = None
    with suppress(TypeError, IndexError):
        number_option = int(input('Selecione uma opção: ')) - 1
        option = options[number_option]
    if option is not None:
        hr()
        option.run()
        console.pause()
    start()


start()
input()
