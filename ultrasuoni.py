import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

trig = 15
echo = 14

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

gpio.output(trig, True)
time.sleep(0.00001)
gpio.output(trig, False)

while gpio.input(echo) == False:
    start = time.time()

while gpio.input(echo) == True:
    end = time.time()

sig_time = end-start

distance = sig_time / 0.000058

print("Distance: {} CM".format(distance))

gpio.cleanup
