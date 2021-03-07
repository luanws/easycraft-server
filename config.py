import os

config = {
    'application_name': 'Easycraft server',
    'path': {
        'ngrok': os.path.join('data', 'ngrok'),
        'server': os.path.join('data', 'server.jar'),
        'ngrok_auth_token': os.path.join('data', 'authtoken.txt')
    },
    'url': {
        'ngrok_login': 'https://dashboard.ngrok.com/get-started/your-authtoken'
    }
}
