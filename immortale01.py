import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

for i in range(12):
	kit.servo[i].angle = 180
	time.sleep(1)
	kit.servo[i].angle = 0
	time.sleep(1)
