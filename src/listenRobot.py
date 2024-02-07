#!/usr/bin/env python3

import time
import pyautogui
from kortex_driver.srv import *
from kortex_driver.msg import *
import os.path
import rospy


class ListeningRobotSimulated:

    def __init__(self):
        self.z = None
        self.y = None
        self.x = None
        self.sub = rospy.Subscriber("/my_gen3/base_feedback", BaseCyclic_Feedback, self.callback)
        rospy.sleep(2)

    def callback(self, msg):
        self.x = msg.base.tool_pose_x
        self.y = msg.base.tool_pose_y
        self.z = msg.base.tool_pose_z


if __name__ == '__main__':
    rospy.init_node("listener")
    robotSimulated = ListeningRobotSimulated()
    rate=rospy.Rate(5)
    while not rospy.is_shutdown():
        if (os.path.isfile("/home/mdossantos/catkin_workspace/src/aat4irs/src/armPosition.txt")):
            f = open("/home/mdossantos/catkin_workspace/src/aat4irs/src/armPosition.txt", "a")
        else:
            f = open("/home/mdossantos/catkin_workspace/src/aat4irs/src/armPosition.txt", "x")

        f.write(str(robotSimulated.x) + "," + str(robotSimulated.y) + "," + str(robotSimulated.z)+"\n")
        rate.sleep()

    f.close()

