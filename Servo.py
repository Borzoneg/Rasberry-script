import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout

# Set up pin 11 for PWM
pins = [3]
pwms = []
i = 0
for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	pwms.append(GPIO.PWM(pin,30))
	pwms[i].start(0)
	i += 1

def SetAngle0(angle):
	duty = angle / 18 + 2
	i = 0
	for pin in pins:
		GPIO.output(pin, True)
		pwms[i].ChangeDutyCycle(duty)
		i += 1
		
	sleep(1)
	i = 0
	for pin in pins:
		GPIO.output(pin, False)
		pwms[i].ChangeDutyCycle(0)  
		i += 1
	
	
def SetAngle(angle, servo):
	duty = angle / 18 + 2
	GPIO.output(servo, True)
	pwms[pins.index(servo)].ChangeDutyCycle(duty)
			
	sleep(0.8)
	
	GPIO.output(servo, True)
	pwms[pins.index(servo)].ChangeDutyCycle(0)  


angle = 0

while True:
	SetAngle0(180)
	SetAngle0(0)


"""
while(angle != -1):
	angle = input("Inserire angolo: ")
	SetAngle0(angle)
"""
"""
while True:
	angle = input("Inserire angolo: ")
	bers = input("Inserire servo da muover: ")
	SetAngle(angle,bers)
"""
# Clean up everything
for pwm in pwms:
	pwm.stop()			# At the end of the program, stop the PWM
GPIO.cleanup()    
    
