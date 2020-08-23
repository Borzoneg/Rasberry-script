"""
Program to move a quadleg robot made out by 3 servos for leg.

Wiring: 

VCC board 	->	pin nr°1 Raspberry(3.3[V])
SDA board 	-> 	pin nr°3 Raspberry(SDA)
SCL board 	-> 	pin nr°5 Raspberry(SCL) 
GND board 	->	pin nr°9 Raspberry(GND)
V+ board 	->	X4 AA battery(6V)

Power up for raspberry provided by ?

"""

import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16) # specify type of board 

angles=[90, 90, 90] # initial setting of servos

for i in range(3):
	kit.servo[i].angle = angles[i]


def moveServo(servoNr, currentAngle, targetAngle): # function to move Servo in way less rough that could cause breaks or problems in general
	while(currentAngle != targetAngle): # continuous cycle to get to the target angle
		if currentAngle < targetAngle: # check if we have to go 'up' or 'down'
			currentAngle += 1
		else: 
			currentAngle -= 1
		kit.servo[servoNr].angle = currentAngle
		time.sleep(0.007)


def straight(leg): # sequence to move the target leg one step forward
	moveServo(leg+1, 90, 70)
	moveServo(leg+0, 90, 120)
	moveServo(leg+2, 90, 130)
	moveServo(leg+1, 70, 90)
	moveServo(leg+0, 120, 90)
	moveServo(leg+2, 130, 90)

while True: # continuous cycle to check for input
	comand = input()
	if(comand=='l'):
		straight(0)
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
	if(comand=='o'):
		kit.servo[2].angle = 180
	if(comand=='p'):
		kit.servo[2].angle = 0
