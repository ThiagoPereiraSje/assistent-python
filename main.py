# salvar dependências: pip freeze > packages
# instalar dependências: pip install -r packages

from functions import listen

# say_english('Hello world!')
# say_portuguese('olá tudo bem')


def start():
    listen()


if __name__ == '__main__':
    start()
