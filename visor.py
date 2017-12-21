from module_gps import get_address, get_nav

def where_am_i():
    address = get_address()
    return address

def get_direction(destination):
    origin = get_address()
    directions = get_nav(origin, destination)

    return directions

