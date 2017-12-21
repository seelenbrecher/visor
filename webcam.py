import os
import requests

url = 'http://139.59.117.49:8083'
file_url = 'capture.jpg'

def capture():
    os.system('fswebcam -d /dev/video0 -r 640x480 --no-banner -S 8 -s brightness=60% capture.jpg')

def get_object_from_image():
    capture()
    files = {'file': open(file_url, 'rb')}

    r = requests.post(url, files=files)

    return r.json()

