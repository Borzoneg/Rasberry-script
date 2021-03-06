import ObjServo


class Immortale:
	def __init__(self):
		reversed_servo = [[-1, 1, -1], [1, -1, 1], [1, -1, 1], [1, 1, 1]]
		self.legs = list()
		self.servos = list()
		for legNr in range(4): 	# with these two cycle i'll create a list where at the position x, y I'll have the
			leg = list() 		# servo in y position on the x leg
			for servoNr in range(3):
				servo = ObjServo.Servo(legNr, servoNr, reversed_servo[legNr][servoNr])
				leg.append(servo)
				self.servos.append(servo)
			self.legs.append(leg)

	def reset(self):
		for servo in self.servos:
			servo.reset()

	def leg_straight_step(self, leg):
		self.legs[leg][1].forward()
		self.legs[leg][2].forward()
		self.legs[leg][0].forward()
		self.legs[leg][1].back()
		self.legs[leg][2].back()

	def leg_back_step(self, leg):
		self.legs[leg][1].back()
		self.legs[leg][2].back()
		self.legs[leg][0].back()
		self.legs[leg][1].forward()

	def leg_crouch(self, leg):
		self.legs[leg][2].set_angle(90)
		self.legs[leg][0].set_angle(90)

	# sequence to move the whole robot one step forward, the robot make a step with each leg and end up as it has started
	def straight_pace(self):
		self.leg_crouch(1)
		self.leg_crouch(2)
		self.leg_straight_step(1)
		self.leg_crouch(0)
		self.leg_crouch(3)
		self.leg_straight_step(0)

	def back_pace(self):
		self.leg_crouch(3)
		self.leg_crouch(0)
		self.leg_straight_step(3)
		self.leg_crouch(2)
		self.leg_crouch(1)
		self.leg_straight_step(2)

	def reverse_servo(self, leg, position):
		self.legs[leg][position].reverse()

	def hard_reset(self):
		for servo in self.servos:
			servo.hard_reset()

	def test(self):
		for servo in self.servos:
			servo.forward()
			servo.back()

	# def clockwise(self):
	# def anti_clockwise(self):
