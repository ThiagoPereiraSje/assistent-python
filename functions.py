import os

# inglês
ENGLISH = 'espeak -s 120 -v us-mbrola-2'

# portugues brasil
PORTUGUESE = 'espeak -s 120 -v brazil-mbrola-1'


def say_english(phrase):
    os.system(ENGLISH + ' "'+phrase+'"')


def say_portuguese(phrase):
    os.system(PORTUGUESE + ' "'+phrase+'"')
