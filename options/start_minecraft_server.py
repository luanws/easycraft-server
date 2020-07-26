from models.option import Option
from utils import styledprint
from utils import ngrok


class StartMinecraftServer(Option):
    name = 'Start minecraft server'

    def run(self):
        ngrok.start()
