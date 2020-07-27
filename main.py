import asyncio

from config import config
from typing import List
from contextlib import suppress
from utils import styledprint, console

from models.option import Option
from options.download_minecraft_server import DownloadMinecraftServer
from options.start_minecraft_server import StartMinecraftServer
from options.publish_server import PublishServer

options: List[Option] = [
    DownloadMinecraftServer(),
    StartMinecraftServer(),
    PublishServer(),
]


async def menu():
    print()
    menu_options = "\n".join([f"({i}) {option.name}" for i, option in enumerate(options, 1)])
    print(styledprint.indent(
        menu_options,
        color=styledprint.Color.CYAN
    ))

    print()
    option = None
    with suppress(Exception):
        number_option = int(input('Selecione uma opção: '))
        option = options[number_option - 1]
    if option is not None:
        console.clear()
        await option.run()


async def start():
    console.clear()
    styledprint.styled_print(
        config['application_name'].upper(),
        color=styledprint.Color.MAGENTA
    )

    await menu()


while True:
    asyncio.run(start())
