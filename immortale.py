from adafruit_servokit import ServoKit
from time import sleep
from inputs import *

kit = ServoKit(channels=16)

a1 = 0
a2 = 1
a3 = 2
b1 = 3
b2 = 4
b3 = 5
c1 = 6
c2 = 7
c3 = 8
d1 = 9
d2 = 10
d3 = 11

# per cambiare il range di angoli del servo da 180° a 160°
# kit.servo[i].actuation_range = 160

#per cambiare pulsazione da un minimo di 1000 a un massimo di 2000
#kit.servo[i].set_pulse_width_range(1000, 2000)

for i in range(10):
	if i in [1, 4, 7, 10]:
		kit.servo[i].angle = 120
	else:
		kit.servo[i].angle = 0

#prototipe della funzione per far camminare avanti il bot
def straight():
	# tira su il servo 1,1;  estende il servo 1,2;
	kit.servo[a1].angle = 120
	kit.servo[a2].angle = 0
	sleep(1)
	# infine riabbassa il servo 1,1
	kit.servo[a1].angle = 0
	sleep(1)

	# tira su il servo 2,1;  estende il servo 2,2;
	kit.servo[b1].angle = 120
	sleep(1)
	kit.servo[b2].angle = 0
	sleep(1)
	# infine riabbassa il servo 2,1
	kit.servo[b1].angle = 0
	sleep(1)
	# tira su il servo 3,1; contrae il servo 3,3 e il servo 3,2;
	# infine riabbassa il servo 3,1

	# tira su il servo 4,1; contrae il servo 4,3 e il servo 4,2;
	# infine riabbassa il servo 4,1

def back(): 
	kit.servo[0].angle = 0
	sleep(1)
	kit.servo[0].angle = 120
	sleep(1)

def clowckwise():
	1+1

def anticlockwise():
	1+1


while True:
	# events = get_gamepad()
	# for event in events:
		# print(event,ev_type, " ", event.code, " ", event.state, "...\n")
	if (1):
		back()

