from models.option import Option
from utils import server
from utils import console, styledprint


class StartServer(Option):
    name = 'Iniciar servidor do Minecraft'

    async def run(self):
        while not server.accept_terms():
            server.start()

        styledprint.styled_print(
            'Termos aceitos com sucesso',
            color=styledprint.Color.GREEN
        )
        styledprint.styled_print(
            'Iniciando servidor Minecraft...',
            color=styledprint.Color.GREEN
        )

        server.start(create_new_console=True)
