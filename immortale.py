"""
Program to move a quadleg robot made out by 3 servos for leg.

Wiring: 

VCC board 	->	pin nr°1 Raspberry(3.3[V])
SDA board 	-> 	pin nr°3 Raspberry(SDA)
SCL board 	-> 	pin nr°5 Raspberry(SCL) 
GND board 	->	pin nr°9 Raspberry(GND)
V+ board 	->	X4 AA battery(6V)

Power up for raspberry provided by ?

Servos enumeration:

  0_1_2-*0*-----*1*-2_1_0
		 |		|
		 |		|
		 |		|
  0_1_2-*2*----*3*-2_1_0

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


def straightStep(leg): # sequence to move the target leg one step forward
	leg *= 3 # leg 0 has the servo 0,1,2; leg 1 has the servo 3+0, 3+1, 3+2 and so... 
	moveServo(leg+1, 90, 70)
	moveServo(leg+0, 90, 120)
	moveServo(leg+2, 90, 130)
	moveServo(leg+1, 70, 90)
	moveServo(leg+0, 120, 90)
	moveServo(leg+2, 130, 90)


def backStep(leg): # sequence to move the target leg one step forward
	leg *= 3 # leg 0 has the servo 0,1,2; leg 1 has the servo 3+0, 3+1, 3+2 and so... 
	moveServo(leg+1, 90, 70)
	moveServo(leg+0, 90, 120)
	moveServo(leg+2, 90, 50)
	moveServo(leg+1, 70, 90)
	moveServo(leg+0, 120, 90)
	moveServo(leg+2, 50, 90)


def straightPace(): # sequence to move the whole robot one step forward, the robot make a step with each leg and end up as it has started
	straightStep(0)
	straightStep(3)
	straightStep(1)
	straightStep(2)


def backPace(): # sequence to move the whole robot one step back, the robot make a step with each leg and end up as it has started
	backStep(0)
	backStep(3)
	backStep(1)
	backStep(2)


def clockwise(): # sequence to move the whole robot one step forward, the robot make a step with each leg and end up as it has started
	straightStep(0)
	backStep(3)
	straightStep(2)
	backtStep(1)


def antiClockwise(): # sequence to move the whole robot one step forward, the robot make a step with each leg and end up as it has started
	backtStep(0)
	straightStep(3)
	backStep(2)
	straighttStep(1)


while True: # continuous cycle to check for input
	comand = input()
	if(comand=='l'):
		straightStep(0)
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
