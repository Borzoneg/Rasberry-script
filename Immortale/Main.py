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
	 	 |		|
		 |		|
		 |		|
  2_1_0-*2*----*3*-0_1_2

"""


# TODO: All the ObjImmortale file, function to init the whole robot object, function to make hit move one pace forward