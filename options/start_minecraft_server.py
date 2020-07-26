from models.option import Option
from utils import styledprint
from utils import ngrok


class StartMinecraftServer(Option):
    name = 'Start minecraft server'

    async def run(self):
        ngrok.ngrok()
