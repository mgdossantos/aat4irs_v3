#!/usr/bin/env python3

import time
from kortex_driver.srv import *
from kortex_driver.msg import *
from RobotActions import ExampleCartesianActionsWithNotifications

arm = ExampleCartesianActionsWithNotifications()

if __name__ == "__main__":
    arm.example_send_gripper_command(0)
    arm.example_home_the_robot()
    #arm.example_send_cartesian_pose(0.5,0.5,0.5,0,0,0)

