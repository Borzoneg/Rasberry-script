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

2_1_0--*0*-----*1*-0_1_2
		|		|
		|		|
		|		|
2_1_0--*3*-----*2*-0_1_2

"""
import ObjImmortale

immortale = ObjImmortale.Immortale()
immortale.reset()

# continuous cycle to check for input
while True:
	command = input()
	if command == 'w':
		immortale.straight_pace()
	if command == 's':
		immortale.back_pace()
	if command == 'r':
		immortale.reset()
	if command == '1':
		leg = int(input("Insert leg: "))
		position = int(input("Insert position: "))
		immortale.reverse_servo(leg, position)
	if command == '2':
		immortale.hard_reset()
