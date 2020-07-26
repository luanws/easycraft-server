from models.option import Option
from utils import ngrok


class PublishServer(Option):
    name = 'Tornar o servidor público'

    async def run(self):
        ngrok.tcp(25565)
