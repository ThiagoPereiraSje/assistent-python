import os
import speech_recognition as sr
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# inglês
ENGLISH = 'espeak -s 120 -v us-mbrola-2'

# portugues brasil
PORTUGUESE = 'espeak -s 120 -v brazil-mbrola-1'


def say_english(phrase):
    os.system(ENGLISH + ' "'+phrase+'"')


def say_portuguese(phrase):
    os.system(PORTUGUESE + ' "'+phrase+'"')


def builtTrainedBot():
    bot = ChatBot('JARVS')
    trainer = ListTrainer(bot)

    for _file in os.listdir('chats'):
        fileLines = open('chats/' + _file, 'r').readlines()
        trainer.train(fileLines)

    return bot


def listenMe():
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)

        try:
            audio = mic.listen(source)
            phrase = mic.recognize_google(audio)
            return phrase
        except sr.UnknownValueError:
            print('oops!')
