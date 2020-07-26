import os

from models.option import Option
from utils import styledprint
from utils import server
from utils import console


class StartMinecraftServer(Option):
    name = 'Start minecraft server'

    async def run(self):
        server.start()
        console.pause()
