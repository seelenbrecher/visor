import os

def text_to_speech(text):
    os.system('google_speech -l id "%s" -e delay 1' %text)

