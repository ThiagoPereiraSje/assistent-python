# salvar dependências: pip freeze > packages
# instalar dependências: pip install -r packages

from functions import listenMe

# say_english('Hello world!')
# say_portuguese('olá tudo bem')


def start():
    phrase = listenMe()
    print('you: ', phrase)


if __name__ == '__main__':
    start()
