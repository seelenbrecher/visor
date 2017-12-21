from module_gps import get_address, get_nav
from webcam import get_object_from_image

def where_am_i():
    address = get_address()
    return address

def get_direction(destination):
    origin = get_address()
    directions = get_nav(origin, destination)

    return directions


def capture():
    objects = get_object_from_image()

    object_count = {}
    for obj in objects:
        key = list(obj.keys())[0]
        if key in object_count:
            object_count[key] += 1
        else:
            object_count[key] = 1

    return object_count
