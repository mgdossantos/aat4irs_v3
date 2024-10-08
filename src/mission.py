#!/usr/bin/env python3
import datetime
import time
from kortex_driver.srv import *
from kortex_driver.msg import *
from RobotActions import ExampleCartesianActionsWithNotifications
from std_msgs.msg import String
import rospy

arm = ExampleCartesianActionsWithNotifications()
cont = 0




if __name__ == "__main__":

    arm.listener()
    arm.example_send_gripper_command(0)
    arm.example_home_the_robot()

    #Mutation 1
    #original code
    arm.example_send_cartesian_pose(0, 0.2, 0, 0, 0, 0)
    #mutant code
    #arm.example_send_cartesian_pose(0, -0.2, 0, 0, 0, 0)

    # Mutation 2
    # original code
    arm.example_send_cartesian_pose(0, 0, 0, 80, 0, 0)
    #arm.example_send_cartesian_pose(0, 0, 0, -80, 0, 0)

    # Mutation 3
    # original code
    arm.example_send_cartesian_pose(0, 0, -0.29, 0, 0, 0)
    # mutant code
    #arm.example_send_cartesian_pose(0, 0, 0.29, 0, 0, 0)

    # Mutation 4
    arm.example_send_gripper_command(1)

    # Mutation 5
    #arm.example_send_gripper_command(1)

    # Mutation 6
    #arm.example_send_gripper_command(0)


    time.sleep(1.5)
    arm.example_home_the_robot()

    # Mutation 7
    # original code
    arm.example_send_cartesian_pose(0, 0, 0, 0, 0, 80)
    # mutant code
    #arm.example_send_cartesian_pose(0, 0, 0, 0, 0, -80)

    arm.example_send_cartesian_pose(0, 0.45, 0, 0, 0, 0)

    # Mutation 8
    # original code
    arm.example_send_cartesian_pose(-0.9, 0, 0, 0, 0, 0)
    # mutant code
    #arm.example_send_cartesian_pose(0.9, 0, 0, 0, 0, 0)


    arm.example_send_cartesian_pose(0, 0, 0, 80, 0, 0)



    arm.example_send_cartesian_pose(0, 0, -0.3, 0, 0, 0)



    if int(arm.sensor) % 2 == 0:

        arm.example_send_cartesian_pose(0, -0.2, 0, 0, 0, 0)

    arm.example_send_gripper_command(0)
    time.sleep(1)
    arm.example_home_the_robot()
