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

    def forward(self, angle=30):
        for i in range(angle):
            self.angle = self.angle + 1 * self.reversed
            kit.servo[self.number].angle = self.angle
            time.sleep(0.007)

    def back(self, angle=30):
        for i in range(angle):
            self.angle = self.angle - 1 * self.reversed
            kit.servo[self.number].angle = self.angle
            time.sleep(0.007)

    def set_angle(self, angle):
        while self.angle != angle:
            if self.angle < angle:
                self.forward(1)
            else:
                self.back(1)

    def hard_reset(self):
        self.set_angle(90)

    def reset(self):
        self.angle = self.startAngle
        self.set_angle(self.angle)

    def get_info(self):
        return "Servo number: {number}; Angle: {angle}; StartAngle: {startAngle}"\
            .format(number=self.number, angle=self.angle, startAngle=self.startAngle)

    def reverse(self):
        self.reversed = -1 if self.reversed == 1 else 1
        if self.startAngle == 135:
            self.startAngle = 45
        elif self.startAngle == 45:
            self.startAngle = 135
