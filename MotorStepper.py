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

seq = [[0,0,0,1], [0,0,1,1], [0,0,1,0], [0,1,1,0], 
        [0,1,0,0], [1,1,0,0], [1,0,0,0], [1,0,0,1]]
     
def clockwise():
    for i in range(len(seq)):
        for j in range (len(seq[i])):
            if(seq[i][j]):
                gpio.output(stepPins[j], True)
               
            else:
                gpio.output(stepPins[j], False)
        time.sleep(0.0007)                      #0.0007 massima velocità

while True:
    clockwise()


"""
seq = [[1,0,0,1], [1,0,0,0], [1,1,0,0], [0,1,0,0], 
        [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1]]
stepCount = len(seq)
stepDir = 1
stepCounter = 0

while True:
    waitTime = input("Quanto e il delay? ")
    waitTime = int(waitTime)/ 10
    print(stepCounter, " ", seq[stepCounter])
    for pin in range(0, 4):
        xpin = stepPins[pin]
        if seq[stepCounter][pin]!= 0:
            gpio.output(xpin, True)
            print("Enable GPIO")
        
        else:
            gpio.output(xpin,False)

        stepCounter += stepDir

        if(stepCounter >= stepCount):
               stepCounter = 0
        if(stepCounter < 0):
               stepCounter = stepCount + stepDir
        time.sleep(waitTime)
"""
