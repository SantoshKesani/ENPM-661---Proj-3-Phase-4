#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
from Astar_rigid import Robot
import math
import sys

def vel_pub():
	rospy.init_node('phase_4', anonymous=True)
	pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)
	rate = rospy.Rate(10)
	R = Robot(((float(sys.argv[1])-3), (float(sys.argv[2])-3), int(math.degrees(float(sys.argv[3])))),
                  ((float(sys.argv[4])), (float(sys.argv[5]))), int(sys.argv[6]), int(sys.argv[7]))
	vels = R.get_velocities()
	command = Twist()
	for i in range(len(vels)):
		command.linear.x= vels[i][0]
		command.angular.z=vels[i][2]
		pub.publish(command)
		rate.sleep()

if __name__ == "__main__":
	while not rospy.is_shutdown():
		vel_pub()
