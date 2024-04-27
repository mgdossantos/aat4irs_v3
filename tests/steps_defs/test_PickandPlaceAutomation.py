
from pytest import *
from pytest_bdd import scenarios, given, when, then,parsers
import time
import pyautogui
import rospy
import os
from kortex_driver.srv import *
from kortex_driver.msg import *
from setup import *
from sensor import *

scenarios('../features/sendBox.feature')
@given("the industrial robotic system is initialized")
def setup_robot():
    setupRobot(1)
@given("the conveyor is initialized")
def setup_conveyor():
   setupConveyor(1)
@given(parsers.cfparse('the robot is at home with the position error threshold being less than or equal "{errorThreshold:Number}" cm in the x-axis'
    , extra_types=dict(Number=float)))
def robot_position_initialX(errorThreshold):
    positionRobot = readSensor(1)
    assert round(abs(0.5761017203330994 - positionRobot[0]),2) <= errorThreshold
@given(parsers.cfparse('the robot is at home with the position error threshold being less than or equal "{errorThreshold:Number}" cm in the y-axis', extra_types=dict(Number=float)))
def robot_position_initialY(errorThreshold):
    positionRobot = readSensor(1)
    assert round(abs(0.0021495665423572063 - positionRobot[1]),2) <= errorThreshold
@given(parsers.cfparse('the robot is at home with the position error threshold being less than or equal "{errorThreshold:Number}" cm in the z-axis', extra_types=dict(Number=float)))
def robot_position_initialZ(errorThreshold):
    positionRobot = readSensor(1)
    assert round(abs(0.434011310338974 - positionRobot[2]),2) <= errorThreshold
@given(parsers.cfparse('the box is in the conveyor with the position error threshold being less than or equal "{errorThreshold:Number}" cm in the x-axis',extra_types=dict(Number=float)))
def box_positionAX(errorThreshold):
    positionBoxInitial= readSensor(2)
    if positionBoxInitial[0] == 'red':
        assert (round(abs(0.5500000541335124 - positionBoxInitial[1]),2)<= errorThreshold)
    else:
        assert (round(abs(0.5500000541335124 - positionBoxInitial[1]),2)<= errorThreshold)
@given(parsers.cfparse('the box is in the conveyor with the position error threshold being less than or equal "{errorThreshold:Number}" cm in the y-axis',extra_types=dict(Number=float)))
def box_positionA(errorThreshold):
    positionBoxInitial= readSensor(2)
    if positionBoxInitial[0] == 'red':
        assert (round(abs(0.19999997215550022 - positionBoxInitial[2]),2)<= errorThreshold)
    else:
        assert (round(abs(0.19999997215550022 - positionBoxInitial[2]),2)<= errorThreshold)
@given(parsers.cfparse('the box is in the conveyor with the position error threshold being less than or equal "{errorThreshold:Number}" cm in the z-axis',extra_types=dict(Number=float)))
def box_positionA(errorThreshold):
    positionBoxInitial= readSensor(2)
    if positionBoxInitial[0] == 'red':
        assert (round(abs(1.000000266368528 - positionBoxInitial[3]),2)<= errorThreshold)
    else:
        assert (round(abs(1.000000266368528 - positionBoxInitial[3]),2)<= errorThreshold)
@when("the pick-and-place finished")
def pickplace_mission():
    pyautogui.hotkey('ctrl', 'alt', 't')

    time.sleep(2)
    pyautogui.write('rosrun aat4irs mission.py')
    pyautogui.press('enter')
    timeout = 35
    ini = time.time()
    now = time.time()

    while now - ini <= timeout:
        time.sleep(1)
        now = time.time()
@then(parsers.cfparse('the box should be in the specific target with the position error threshold being less than or equal "{errorThreshold:Number}" cm in the x-axis',extra_types=dict(Number=float)))
def box_positionBX(errorThreshold):
    pyautogui.hotkey('ctrl', 'alt', 't')
    positionBoxFinal = readSensor(3)
    if positionBoxFinal[0] == 'red':
        assert (round(abs(-0.3252519529197406 - positionBoxFinal[1]), 2) <= errorThreshold)
    else:
        assert (round(abs(-0.31896505436911077 - positionBoxFinal[1]), 2) <= errorThreshold)
@then(parsers.cfparse('the box should be in the specific target with the position error threshold being less than or equal "{errorThreshold:Number}" cm in the y-axis',extra_types=dict(Number=float)))
def box_positionBY(errorThreshold):
    pyautogui.hotkey('ctrl', 'alt', 't')
    positionBoxFinal = readSensor(3)
    if positionBoxFinal[0] == 'red':
        assert (round(abs(0.22059896163617632 - positionBoxFinal[2]), 2) <= errorThreshold)
    else:
        assert (round(abs(0.43548827869933354 - positionBoxFinal[2]), 2) <= errorThreshold)
@then(parsers.cfparse('the box should be in the specific target with the position error threshold being less than or equal "{errorThreshold:Number}" cm in the z-axis',extra_types=dict(Number=float)))
def box_positionBZ(errorThreshold):
    pyautogui.hotkey('ctrl', 'alt', 't')
    positionBoxFinal = readSensor(3)
    if positionBoxFinal[0] == 'red':
        assert (round(abs(0.7675001885747819 - positionBoxFinal[3]), 2) <= errorThreshold)
    else:
        assert (round(abs(0.7683375216119632 - positionBoxFinal[3]), 2) <= errorThreshold)
