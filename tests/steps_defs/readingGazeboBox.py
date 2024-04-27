#!/usr/bin/env python3

from gazebo_msgs.srv import GetModelState
import rospy
import time
import os.path




class Block:
    def __init__(self, name, relative_entity_name):
        self._name = name
        self._relative_entity_name = relative_entity_name

class ListeningBox:

    _blockListDict = {
        'red_box': Block('red_box', 'red_box'),
        'blue_box': Block('blue_box', 'blue_box'),

    }

    def __init__(self):
        rospy.init_node('get_box_position')

    def show_gazebo_models(self):
        try:
            model_coordinates = rospy.ServiceProxy("/gazebo/get_model_state", GetModelState)
            rospy.wait_for_service("/gazebo/get_model_state")

            for block in self._blockListDict.values():
                blockName = str(block._name)
                resp_coordinates = model_coordinates(blockName, block._relative_entity_name)

                if resp_coordinates.success==True and blockName == 'red_box':
                    self.state = model_coordinates(model_name="red_box")
                    self.color = blockName.split('_')[0]
                    self.x = self.state.pose.position.x
                    self.y = self.state.pose.position.y
                    self.z = self.state.pose.position.z
                if resp_coordinates.success==True and blockName == 'blue_box':
                    self.state = model_coordinates(model_name="blue_box")
                    self.color = blockName.split('_')[0]
                    self.x = self.state.pose.position.x
                    self.y = self.state.pose.position.y
                    self.z = self.state.pose.position.z


        except rospy.ServiceException as e:
            rospy.loginfo("Get Model State service call failed:  {0}".format(e))




if __name__ == '__main__':

    try:
        box = ListeningBox()
        box.show_gazebo_models()
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
