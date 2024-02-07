from setup import *
import numpy
import random
import os.path

def noise():
    mean = 0
    std = 1
    num_samples = 1000
    samples = numpy.random.normal(mean, std, size=num_samples)
    n = random.randint(0,99)
    return samples[n]

def readSensor(typeSensor):
    time.sleep(2)
    #if typeSensor != 1:
    if typeSensor == 1:
        typeName = 'readingGazeboRobot'
        lineExecution = 'rosrun aat4irs ' + typeName + '.py'
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(2)
        pyautogui.press('enter')
        pyautogui.write(lineExecution)
        pyautogui.press('enter')
        time.sleep(5)
        logSensor = '/home/mdossantos/catkin_workspace/src/aat4irs/tests/steps_defs/armPosition.txt'
        with open(logSensor, 'r') as input_file:
            for line in input_file:
                pass
            text = line
        positionRobot = text.split(",")
        positionRobotX = float(positionRobot[0])
        #positionRobotX = float(positionRobot[1])
        positionRobotY = float(positionRobot[1])
        positionRobotZ = float(positionRobot[2])

        #noiseSample= noise()
        noiseSample=0
        positionRobotX = positionRobotX+ noiseSample

        #noiseSample = noise()
        noiseSample=0
        positionRobotY = positionRobotY + noiseSample

        #noiseSample = noise()
        noiseSample=0
        positionRobotZ = positionRobotZ + noiseSample

        return positionRobotX,positionRobotY,positionRobotZ

    if typeSensor == 2:

        typeName = 'readingGazeboBox'
        lineExecution = 'rosrun aat4irs ' + typeName + '.py'
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(2)
        pyautogui.press('enter')
        pyautogui.write(lineExecution)
        pyautogui.press('enter')
        time.sleep(5)
        with open('/home/mdossantos/catkin_workspace/src/aat4irs/tests/steps_defs/boxPosition.txt','r') as input_file:
            for line in input_file:
                pass
            text = line
        positionBox = text.split(",")
        color = positionBox[0]
        positionBoxX = float(positionBox[1])
        positionBoxY = float(positionBox[2])
        positionBoxZ = float(positionBox[3])



        # noiseSample= noise()
        noiseSample = 0
        positionBoxX= positionBoxX + noiseSample

        #noiseSample = noise()
        noiseSample=0
        positionBoxY= positionBoxY + noiseSample

        #noiseSample = noise()
        noiseSample = 0
        positionBoxZ= positionBoxZ + noiseSample

        return color,positionBoxX, positionBoxY, positionBoxZ



    if typeSensor == 3:
        typeName = 'readingGazeboBoxFinal'
        lineExecution= 'rosrun aat4irs '+ typeName+'.py'
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(2)
        pyautogui.press('enter')
        pyautogui.write(lineExecution)
        pyautogui.press('enter')
        time.sleep(5)

        with open('/home/mdossantos/catkin_workspace/src/aat4irs/tests/steps_defs/boxPositionFinal.txt','r') as input_file:
            for line in input_file:
                pass
            text = line
        positionFinalBox = text.split(",")
        color = positionFinalBox[0]
        positionFinalBoxX = float(positionFinalBox[1])
        positionFinalBoxY = float(positionFinalBox[2])
        positionFinalBoxZ = float(positionFinalBox[3])

        noiseSample= noise()
        #noiseSample = 0
        positionFinalBoxX = positionFinalBoxX + noiseSample

        noiseSample = noise()
        #noiseSample = 0
        positionFinalBoxY = positionFinalBoxY + noiseSample

        noiseSample = noise()
        #noiseSample = 0

        positionFinalBoxZ = positionFinalBoxZ + noiseSample


        return color, positionFinalBoxX, positionFinalBoxY, positionFinalBoxZ

        #finalizeSystem(1)

