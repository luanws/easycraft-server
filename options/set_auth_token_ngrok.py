from models.option import Option
from utils import ngrok


class SetAuthTokenNgrok(Option):
    name = 'Definir authtoken do ngrok'

    async def run(self):
        auth_token = ngrok.request_auth_token()
        ngrok.save_auth_token(auth_token)
        ngrok.login(auth_token)
