import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

angles=[90, 90, 90]

for i in range(3):
	kit.servo[i].angle = angles[i]

while True:
	comand = input()
	if(comand=='l'):
		straight()
	if(comand=='q'):
		angles[0] += 5
		kit.servo[0].angle = angles[0]
	if(comand=='w'):
		angles[1] += 5
		kit.servo[1].angle = angles[1]
	if(comand=='e'):
		angles[2] += 5
		kit.servo[2].angle = angles[2]
	if(comand=='a'):
		angles[0] -= 5
		kit.servo[0].angle = angles[0]
	if(comand=='s'):
		angles[1] -= 5
		kit.servo[1].angle = angles[1]
	if(comand=='d'):
		angles[2] -= 5
		kit.servo[2].angle = angles[2]
	

def straight():
	kit.servo[1].angle = 70
	kit.servo[0].angle = 120
	kit.servo[2].angle = 130
	kit.servo[2].angle = 90
	kit.servo[1].angle = 90
	kit.servo[0].angle = 90
	