from models.option import Option
from utils import server


class StartMinecraftServer(Option):
    name = 'Iniciar servidor do Minecraft'

    async def run(self):
        server.start()
