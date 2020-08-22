import RPi.GPIO as GPIO  
from time import sleep   
GPIO.setmode(GPIO.BOARD) 

GPIO.setwarnings(False)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	if GPIO.input(10) == GPIO.HIGH:
		print("pulsante 2")
	if GPIO.input(8) == GPIO.HIGH:
		print("pulsante 1")
