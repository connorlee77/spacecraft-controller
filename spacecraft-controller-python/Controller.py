import numpy as np

class Controller:

	# Kp - 3x3 matrix
	# Kd - 3x# matrix
	def __init__(self, Kp, Kd):
		self.Kp = Kp
		self.Kd = Kd

	# all input 3x1 vectors
	def u(self, xd, xdotd, x, xdot):
		return -self.Kd*(xdot - xdotd) - self.Kp*(x - xd)

def test():
	ctrl = Controller(np.eye(3), np.eye(3))
	print(ctrl.u(np.ones((3,1)), np.ones((3,1)), np.ones((3,1)), np.ones((3,1))))

if __name__ == "__main__":
    test()
