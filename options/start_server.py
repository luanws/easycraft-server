import os
from models.option import Option
from utils import server
from utils import console
from utils import styledprint
from config import config

server_path = config['path']['server']


class StartServer(Option):
    name = 'Iniciar servidor do Minecraft'

    async def run(self):
        try:
            if not os.path.isfile(server_path):
                raise FileNotFoundError('Minecraft server não encontrado!')
            while not server.accept_terms():
                server.start()

            styledprint.success('Termos aceitos com sucesso')
            styledprint.info('Iniciando servidor Minecraft...')

            server.set_property('online-mode', 'false')
            server.start(create_new_console=True)
        except Exception as e:
            styledprint.danger(e)
            console.pause()
