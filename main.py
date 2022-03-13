# salvar dependências: pip freeze > packages
# instalar dependências: pip install -r packages

from functions import listenMe, createBot, say_english

# say_english('Hello world!')
# say_portuguese('olá tudo bem')


def start():
    bot = createBot()
    i = 0

    while(i < 5):
        i += 1
        phrase = listenMe()
        print('you: ', phrase)

        try:
            botResponse = bot.get_response(phrase)
            print('bot:', botResponse)
            say_english(str(botResponse))
        except bot.ChatBotException:
            say_english('say something')


if __name__ == '__main__':
    start()
