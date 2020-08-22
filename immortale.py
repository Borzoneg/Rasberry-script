import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

angles=[90, 90, 90]

for i in range(3):
	kit.servo[i].angle = angles[i]

def moveServo(servo, currentAngle, targetAngle):
	while(currentAngle != targetAngle):
		currentAngle += 5
		servo.angle(currentAngle)
		time.wait(0.5)


def straight(leg):
	moveServo(kit.servo[leg+1], 90, 70)
	moveServo(kit.servo[leg+0], 90, 120)
	moveServo(kit.servo[leg+2], 90, 130)
	moveServo(kit.servo[leg+2], 70, 90)
	moveServo(kit.servo[leg+1], 120, 90)
	moveServo(kit.servo[leg+0], 130, 90)

kit.servo[i].set_pulse_width_range(1000)

while True:
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
	

	