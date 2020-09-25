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

  2_1_0-*0*-----*1*-0_1_2
	 |	|
	 |	|
	 |	|
  2_1_0-*2*----*3*-0_1_2

"""

import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16) # specify type of board 

def reset():
	resetAngle = 90 # initial setting of servos
	servos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for servo in servos:
		kit.servo[servo].angle = resetAngle
	
	moveServo(0, 90, 45)
	moveServo(4, 90, 135)
	moveServo(8, 90, 45)


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
	moveServo(leg+1, 90, 110)
	moveServo(leg+2, 90, 60)
	moveServo(leg+0, 90, 60)
	moveServo(leg+1, 110, 90)
	"""
	moveServo(leg+0, 120, 90)
	moveServo(leg+2, 130, 90)
	"""

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

reset()
while True: # continuous cycle to check for input
	comand = input()
	if(comand=='w'):
		straightStep(0)
	if(comand=='r'):
		reset()
	if(comand=='t'):
		moveServo(2, 90, 95)
