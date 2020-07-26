from models.option import Option


class DownloadMinecraftServer(Option):
    name = 'Atualizar servidor do minecraft'

    async def run(self):
        print('Fazendo download')
