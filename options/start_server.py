from models.option import Option
from utils import server
from utils import console, styledprint


class StartServer(Option):
    name = 'Iniciar servidor do Minecraft'

    async def run(self):
        while not server.accept_terms():
            server.start()

        styledprint.success('Termos aceitos com sucesso')
        styledprint.info('Iniciando servidor Minecraft...')

        server.set_property('online-mode', 'false')
        server.start(create_new_console=True)
