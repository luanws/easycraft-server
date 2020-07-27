import re
from models.option import Option
from utils import ngrok
from utils import styledprint
from utils import server


def get_port() -> int:
    port = int(server.get_property('server-port'))
    return port


class PublishServer(Option):
    name = 'Tornar o servidor público'

    async def run(self):
        try:
            port = get_port()
            ngrok.tcp(port)
        except Exception as e:
            styledprint.styled_print(e, color=styledprint.Color.RED)
