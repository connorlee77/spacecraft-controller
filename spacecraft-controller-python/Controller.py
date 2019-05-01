import numpy as np
import roslib
import rospy

class Controller:

	# Controller gains
	# Kp - 3x3 matrix
	# Kd - 3x3 matrix
	def __init__(self, Kp=np.eye(3), Kd=np.eye(3)):
		self.Kp = Kp
		self.Kd = Kd

		# initiliaze
        rospy.init_node('SpacecraftController', anonymous=False)
        # tell user how to stop TurtleBot
        rospy.loginfo("To stop the node hit CTRL + C")
        # What function to call when you ctrl + c    
        rospy.on_shutdown(self.shutdown)

		# Trajectory subscriber
		# self.subNavdata = rospy.Subscriber('/ardrone/navdata', trajectoryData, callback) 	
		
		# Current state subscriber
		self.subNavdata = rospy.Subscriber('/ardrone/navdata', stateData, self.u) 	
		
		# Controls input publisher
		self.publisher = rospy.Publisher('/ardrone/land', x)

		# Wait until we receive messages to process in the callback functions
        rospy.spin()

	# data[xd, xdotd, x, xdot] 3x1 vectors
	# output - 3x1
	def u(self, data):
		xd = data.xd
		xdotd = data.xdotd
		x = data.x
		xdot = data.xdot

		return -self.Kd*(xdot - xdotd) - self.Kp*(x - xd)

def test():
	ctrl = Controller(np.eye(3), np.eye(3))
	print(ctrl.u(np.ones((3,1)), np.ones((3,1)), np.ones((3,1)), np.ones((3,1))))

if __name__ == "__main__":
    test()
