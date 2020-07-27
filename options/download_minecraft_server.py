import requests
import time
from urllib import request
from models.option import Option
from bs4 import BeautifulSoup
from bs4.element import Tag
from utils import styledprint
from utils import console

server_path = 'data/server.jar'
minecraft_server_download_page_url = 'https://www.minecraft.net/pt-br/download/server/'


def download_server(url: str):
    request.urlretrieve(url, server_path)


def get_url_server(minecraft_server_download_page_url: str) -> str:
    response = requests.get(minecraft_server_download_page_url)
    beautiful_soup = BeautifulSoup(response.text, 'html.parser')
    a: Tag = beautiful_soup.find('a', {'aria-label': 'mincraft version'})
    return a['href']


class DownloadMinecraftServer(Option):
    name = 'Atualizar o Minecraft server'

    async def run(self):
        try:
            styledprint.info('Buscando endereço do novo servidor na página do minecraft...')
            url = get_url_server(minecraft_server_download_page_url)
            styledprint.success(f'O endereço {url} foi encontrado')
            styledprint.info('Fazendo download do arquivo...')
            download_server(url)
            styledprint.success('Download concluído')
            time.sleep(1)
        except Exception as e:
            styledprint.danger(e)
            console.pause()
