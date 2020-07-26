from models.option import Option


class DownloadMinecraftServer(Option):
    name = 'Download minecraft server'

    def run(self):
        print('Fazendo download')
