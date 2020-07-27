import shutil
import os
from models.option import Option
from contextlib import suppress
from utils import styledprint
from utils import console


class DeleteServer(Option):
    name = 'Deletar servidor'

    async def run(self):
        try:
            files = (
                'banned-ips.json',
                'banned-players.json',
                'eula.txt',
                'ops.json',
                'server.properties',
                'usercache.json',
                'whitelist.json',
            )
            folders = (
                'world',
                'logs',
            )

            for file in files:
                with suppress(FileNotFoundError):
                    os.remove(file)
            for folder in folders:
                with suppress(FileNotFoundError):
                    shutil.rmtree(folder)
            styledprint.success('Servidor deletado com sucesso')
            console.pause()
        except Exception as e:
            styledprint.styled_print(e, color=styledprint.Color.RED)
            console.pause()
