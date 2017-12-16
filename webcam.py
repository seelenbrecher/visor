import os


def capture():
    os.system('fswebcam -d /dev/video0 -r 640x480 --no-banner -S 8 -s brightness=60% capture.jpg')


capture()
