import requests
import subprocess
import gps
import re

API_URL = "https://maps.googleapis.com/maps/api/{}/json?"
API_KEY = "&key=AIzaSyCW1kWt0sYBImC-YKgcaQi_IV6MHNVCoVk"
URL_NAV = "mode={}&origin={}&destination={}&language=id"
URL_GEOCODE = "latlng={},{}"
VOICE = ['google_speech', '-l', 'id', '-e', 'speed', '0.9']

TAG_RE = re.compile(r'<[^>]+>')

def get_address():
    lat, lng = get_lat_lng()
    # lat = -6.364600
    # lng = 106.828684
    url = API_URL.format("geocode") + URL_GEOCODE.format(lat, lng) + API_KEY
    r = requests.get(url)
    if r.json()["status"] == "OK":
        return (r.json()["results"][0]["formatted_address"])
    else:
        return ("ZERO_RESULT")

def get_nav(origin, destination):
    origin = origin.replace(" ", "+")
    destination = destination.replace(" ", "+")
    url = API_URL.format("directions") + URL_NAV.format("walking", origin, destination) + API_KEY
    r = requests.get(url)

    directions = []
    if r.json()["status"] == "OK":
        for route in r.json()['routes'][0]['legs'][0]['steps']:
            direction = {}
            direction['instruction'] = TAG_RE.sub('', route['html_instructions'])
            direction['instruction'] = direction['instruction'].replace('&nbsp;', ' ')
            direction['duration'] = route['duration']['text'].split(' ')[0]
            directions.append(direction)

    return directions

def get_lat_lng():
    gpsd = gps.gps()
    gpsd.stream(gps.WATCH_ENABLE|gps.WATCH_NEWSTYLE)

    for report in gpsd:
        if report['class'] == 'TPV':
            return report['lat'], report['lon']

