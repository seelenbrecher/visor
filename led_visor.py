import RPi.GPIO as GPIO
import time

def light(pin, param):
  io = lambda x: GPIO.HIGH if x == 'on' else GPIO.LOW
  GPIO.output(pin, io(param))

def blink(pin):
  light(pin, 'on')
  time.sleep(0.5)
  light(pin, 'off')
  time.sleep(0.5)

def init_output(pins):
  for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

GPIO.setmode(GPIO.BOARD)
