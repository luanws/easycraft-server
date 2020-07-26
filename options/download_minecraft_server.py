from models.option import Option


class DownloadMinecraftServer(Option):
    def __init__(self):
        super().__init__('Download minecraft server')

    def run(self):
        print('Fazendo download')
