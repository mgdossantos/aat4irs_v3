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

    nameLogFile = "/home/mdossantos/catkin_workspace/src/aat4irs/tests/steps_defs/noise.txt"
    if (os.path.isfile(nameLogFile)):
        f = open(nameLogFile, "a")
    else:
        f = open(nameLogFile, "x")

    f.write(str(samples[n])+"\n")
    f.close()
    return samples[n]

def readSensor(typeSensor):
    time.sleep(2)

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

        #Mutant 9
        #original code
        positionRobotX = float(positionRobot[0])
        #mutant code
        #positionRobotX = -float(positionRobot[0])

        # Mutant 10
        # original code
        positionRobotY = float(positionRobot[1])
        # mutant code
        #positionRobotY = -float(positionRobot[1])

        #Mutant 11
        # original code
        positionRobotZ = float(positionRobot[2])
        # mutant code
        #positionRobotZ = -float(positionRobot[2])

        # Mutant 12
        #noiseSample= noise()
        #positionRobotX = positionRobotX+ noiseSample

        # Mutant 13
        #noiseSample = noise()
        #positionRobotY = positionRobotY + noiseSample


        # Mutant 14
        #noiseSample = noise()
        #positionRobotZ = positionRobotZ + noiseSample

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

        # Mutant 15
        # original code
        positionBoxX = float(positionBox[1])
        # mutant code
        #positionBoxX = -float(positionBox[1])

        # Mutant 16
        # original code
        positionBoxY = float(positionBox[2])
        # mutant code
        #positionBoxY = -float(positionBox[2])

        # Mutant 17
        # original code
        positionBoxZ = float(positionBox[3])
        # mutant code
        #positionBoxZ = -float(positionBox[3])

        # Mutant 18
        #noiseSample = noise()
        #positionBoxX= positionBoxX + noiseSample

        # Mutant 19
        #noiseSample= noise()
        #positionBoxY= positionBoxY + noiseSample

        # Mutant 20
        #noiseSample= noise()
        #positionBoxZ= positionBoxZ + noiseSample

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

        # Mutant 21
        # original code
        #rosrun aat4irs initialization.py
        positionFinalBoxX = float(positionFinalBox[1])
        # mutant code
        #positionFinalBoxX = -float(positionFinalBox[1])

        # Mutant 22
        # original code
        positionFinalBoxY = float(positionFinalBox[2])
        # mutant code
        #positionFinalBoxY = -float(positionFinalBox[2])

        # Mutant 23
        # original code
        positionFinalBoxZ = float(positionFinalBox[3])
        # mutant code
        #positionFinalBoxZ = -float(positionFinalBox[3])

        # Mutant 24
        #noiseSample = noise()
        #positionFinalBoxX= positionFinalBoxX + noiseSample

        # Mutant 25
        #noiseSample= noise()
        #positionFinalBoxY= positionFinalBoxY + noiseSample

        # Mutant 26
        #noiseSample= noise()
        #positionFinalBoxZ= positionFinalBoxZ + noiseSample

        return color, positionFinalBoxX, positionFinalBoxY, positionFinalBoxZ

        #finalizeSystem(1)

