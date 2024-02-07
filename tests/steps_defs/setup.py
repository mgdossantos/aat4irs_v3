import time
import pyautogui


def setupRobot(typeRobot):
    #if typeRobot != 1:
    if typeRobot == 1:

        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(2)
        pyautogui.write('roslaunch aat4irs spawn_kortex_robot.launch')
        pyautogui.press('enter')
        time.sleep(17)
        pyautogui.hotkey('ctrl', 'alt', 't')

        time.sleep(2)
        pyautogui.write('rosrun aat4irs initialization.py')
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'shift', 'q')
        pyautogui.press('enter')

def setupConveyor (typeConveyor):
    if typeConveyor == 1:
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(2)
        pyautogui.write('rosrun  aat4irs box.py')
        pyautogui.press('enter')
        time.sleep(2)


def finalizeSystem(typeSystem):
    if typeSystem==1:
        pyautogui.hotkey('ctrl', 'shift', 'q')
        pyautogui.hotkey('ctrl', 'shift', 'q')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('ctrl', 'shift', 'q')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'shift', 'q')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'shift', 'q')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'shift', 'q')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'alt', 't')

    if typeSystem==2:
        pyautogui.hotkey('ctrl', 'shift', 'q')
        pyautogui.hotkey('ctrl', 'shift', 'q')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(35)
        pyautogui.hotkey('ctrl', 'shift', 'q')





