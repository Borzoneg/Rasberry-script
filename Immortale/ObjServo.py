import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16) # specify type of board

class Servo:
    def __init__(self, leg, position, reversed=1): # reversed can be 1 or -1 if the servo is reversed
        self.position = position
        self.leg = leg
        self.number = position + 4 * leg
        self.reversed = reversed
        if position == 0:
            self.startAngle = 90 + reversed * 45
        else:
            self.startAngle = 90
        self.angle = -1 # angle not set yet


    def reset(self):
        self.angle = self.startAngle
        kit.servo[self.number].angle = self.startAngle


    def forward(self, angle=30):
        for i in range(angle):
            kit.servo[self.number].angle = self.angle + 1 * self.reversed
            time.sleep(0.007)


    def back(self, angle=30):
        for i in range(angle):
            kit.servo[self.number].angle = self.angle - 1 * self.reversed
            time.sleep(0.007)


    def getInfo(self):
        return "Servo number: {number}; Angle: {angle}; StartAngle: {startAngle}"\
            .format(number=self.number, angle=self.angle, startAngle=self.startAngle)
