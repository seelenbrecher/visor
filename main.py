import time
from google_speech import text_to_speech
from module_gps import get_address, get_nav

def where_am_i():
    address = get_address()
    text_to_speech(address)
    return

def get_direction(origin, destination):
    directions = get_nav(origin, destination)

    for direction in directions:
        instruction = direction['instruction']
        duration = direction['duration']

        text_to_speech(instruction)
        time.sleep(int(duration))


get_direction('Fakultas Ilmu Komputer', 'Margocity')
