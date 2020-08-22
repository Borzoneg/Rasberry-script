import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

while true:
	comand = input()
	if(comand=='q'):
		angle0 += 1
		kit.servo[0].angle = angle0 
	if(comand=='w'):
		angle1 += 1
		kit.servo[1].angle = angle1
	if(comand=='e'):
		angle2 += 1
		kit.servo[2].angle = angle2
	if(comand=='a'):
		angle0 -= 1
		kit.servo[0].angle = angle0
	if(comand=='s'):
		angle1 -= 1
		kit.servo[1].angle = angle1
	if(comand=='d'):
		angle2 -= 1
		kit.servo[2].angle = angle2
	