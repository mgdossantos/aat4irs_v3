#!/usr/bin/env python3

import rospy
import time

from kortex_driver.srv import *
from kortex_driver.msg import *
import os.path


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

    if os.path.isfile("/home/mdossantos/catkin_workspace/src/aat4irs/tests/steps_defs/armPosition.txt"):
        f = open("/home/mdossantos/catkin_workspace/src/aat4irs/tests/steps_defs/armPosition.txt", "a")
    else:
        f = open("/home/mdossantos/catkin_workspace/src/aat4irs/tests/steps_defs/armPosition.txt", "x")
    rospy.init_node("listener")
    robotSimulated = ListeningRobotSimulated()
    f.write(str(robotSimulated.x) + "," + str(robotSimulated.y) + "," + str(robotSimulated.z) + "\n")
    f.close()
    time.sleep(2)
