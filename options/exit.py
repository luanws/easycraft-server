from models.option import Option


class Exit(Option):
    name = 'Sair'

    def run(self):
        exit()
