#!/usr/bin/env python3

from gazebo_msgs.srv import GetModelState
import rospy
import time
import os.path

class ListeningBox:
    def __init__(self):

        rospy.init_node('get_box_position')
        g_get_state = rospy.ServiceProxy("/gazebo/get_model_state", GetModelState)
        rospy.wait_for_service("/gazebo/get_model_state")
        try:
            self.state = g_get_state(model_name="red_box")
            self.color='red'
            if self.state.pose.position.x==0.0 and self.state.pose.position.y==0.0 and self.state.pose.position.z==0.0 :
                self.state = g_get_state(model_name="blue_box")
                self.color='blue'
        except Exception as e:
            rospy.logerr('Error on calling service: %s', str(e))
            return


        self.x = self.state.pose.position.x
        #self.y = self.state.pose.position.x
        self.y = self.state.pose.position.y
        self.z = self.state.pose.position.z



if __name__ == '__main__':

    try:
        box = ListeningBox()
    except rospy.ROSInterruptException:
        pass

    nameLogFile = "/home/mdossantos/catkin_workspace/src/aat4irs/tests/steps_defs/boxPosition.txt"
    if (os.path.isfile(nameLogFile)):
        f = open(nameLogFile, "a")
    else:
        f = open(nameLogFile, "x")

    f.write(box.color+","+str(box.x) + "," + str(box.y) + "," + str(box.z) + "\n")
    f.close()
    time.sleep(2)
