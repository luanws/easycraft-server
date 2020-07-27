import os

config = {
    'application_name': 'Minecraft server',
    'path': {
        'ngrok': os.path.join('data', 'ngrok'),
        'server': os.path.join('data', 'server.jar'),
    }
}
