import os
import speech_recognition as sr

# inglês
ENGLISH = 'espeak -s 120 -v us-mbrola-2'

# portugues brasil
PORTUGUESE = 'espeak -s 120 -v brazil-mbrola-1'


def say_english(phrase):
    os.system(ENGLISH + ' "'+phrase+'"')


def say_portuguese(phrase):
    os.system(PORTUGUESE + ' "'+phrase+'"')


def listen():
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)

        try:
            audio = mic.listen(source)
            phrase = mic.recognize_google(audio)
            print('you said: ', phrase)
        except sr.UnknownValueError:
            print('oops!')
