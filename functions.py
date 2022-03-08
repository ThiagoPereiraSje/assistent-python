import os

ESPEAKER = 'espeak -s 120 -v us-mbrola-2'


def say(phrase):
    os.system(ESPEAKER + ' "'+phrase+'"')
