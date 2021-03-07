import asyncio
from options.set_auth_token_ngrok import SetAuthTokenNgrok

from config import config
from typing import Tuple
from contextlib import suppress
from utils import styledprint, console

from models.option import Option
from options.download_minecraft_server import DownloadMinecraftServer
from options.start_server import StartServer
from options.publish_server import PublishServer
from options.delete_server import DeleteServer

options: Tuple[Option] = (
    DownloadMinecraftServer(),
    StartServer(),
    PublishServer(),
    DeleteServer(),
    SetAuthTokenNgrok(),
)


async def run_option(number_option: int):
    option = None
    with suppress(Exception):
        option = options[number_option - 1]
    if option is not None:
        console.clear()
        await option.run()


async def menu():
    print()
    menu_options = "\n".join(
        [f"({i}) {option.name}" for i, option in enumerate(options, 1)])
    print(styledprint.indent(
        menu_options,
        color=styledprint.Color.CYAN
    ))

    print()
    with suppress(Exception):
        commands = input('Selecione uma opção: ')
        try:
            commands = [int(commands)]
        except:
            commands = commands.replace(',', ' ')
            while commands.__contains__('  '):
                commands = commands.replace('  ', ' ')
            commands = [int(c) for c in commands.split()]

        for number_option in commands:
            await run_option(number_option)


async def start():
    console.clear()
    styledprint.styled_print(
        config['application_name'].upper(),
        color=styledprint.Color.MAGENTA,
        attrs=[styledprint.Attribute.BOLD]
    )

    await menu()


while True:
    asyncio.run(start())
