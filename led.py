import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(4,gpio.OUT)

gpio.output(4, gpio.HIGH)
time.sleep(3)
gpio.output(4, gpio.LOW)

gpio.cleanup()
