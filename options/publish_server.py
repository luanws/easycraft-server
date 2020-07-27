import re
from models.option import Option
from utils import ngrok
from utils import styledprint


def get_port() -> int:
    with open('server.properties') as f:
        properties = f.read()
        port = re.findall(r'server-port=(\d+)', properties)[0]
        return int(port)


class PublishServer(Option):
    name = 'Tornar o servidor público'

    async def run(self):
        try:
            port = get_port()
            ngrok.tcp(port)
        except Exception as e:
            styledprint.styled_print(e, color=styledprint.Color.RED)
