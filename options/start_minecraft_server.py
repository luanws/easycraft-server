from models.option import Option
from utils import server


class StartMinecraftServer(Option):
    name = 'Start minecraft server'

    async def run(self):
        server.start()
