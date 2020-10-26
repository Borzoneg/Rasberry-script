import RPi. GPIO  as  gpio
import time

gpio.setmode( gpio.BCM)
gpio.setwarnings(False)

stepPins = [14, 15, 17, 18]
in1 = 14
in2 = 15
in3 = 17
in4 = 18

gpio.setup(in1,  gpio.OUT)
gpio.setup(in2,  gpio.OUT)
gpio.setup(in3,  gpio.OUT)
gpio.setup(in4,  gpio.OUT)


def rotate(oriantation):
    if oriantation == 'c':
        seq = [[0,0,0,1], [0,0,1,1], [0,0,1,0], [0,1,1,0], 
               [0,1,0,0], [1,1,0,0], [1,0,0,0], [1,0,0,1]]
    else:
        seq = [[1,0,0,1], [1,0,0,0], [1,1,0,0], [0,1,0,0], 
               [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1]]

    for i in range(len(seq)):
        for j in range (len(seq[i])):
            if(seq[i][j]):
                gpio.output(stepPins[j], True)
               
            else:
                gpio.output(stepPins[j], False)
        time.sleep(0.001)                      #0.0007 massima velocità

while True:
    comand = input()
    if(comand == 'd'):
        for i in range(30):
            rotate('c')
    if(comand == 'a'):
        for i in range(30):
            rotate('a')
