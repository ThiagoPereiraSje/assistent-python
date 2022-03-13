# salvar dependências: pip freeze > packages
# instalar dependências: pip install -r packages

from functions import listenMe, builtTrainedBot

# say_english('Hello world!')
# say_portuguese('olá tudo bem')


def start():
    bot = builtTrainedBot()
    phrase = listenMe()
    print('you: ', phrase)


if __name__ == '__main__':
    start()
