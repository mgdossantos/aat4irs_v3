#!/usr/bin/env python3
import tf.transformations
from gazebo_msgs.srv import SpawnModel
import rospy
from geometry_msgs.msg import Pose, Quaternion, Point
import random
from std_msgs.msg import String


def main():
    pub = rospy.Publisher('listener', String, queue_size=10)
    rospy.init_node('box', log_level=rospy.INFO)
    rospy.wait_for_service("/gazebo/spawn_sdf_model")
    #Hz
    rate=rospy.Rate(10)
    spawn_model_client = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
    orient = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0))
    sensor=random.randint(1,10)
    #sensor = 2
    print(sensor)
    position = Point(0.55, 0.2, 1)
    # to simulate the sensor read. cont is odd means read sensor is red
    #if sensor % 2 != 0:
    if sensor%2==0:
        modelName = 'red_box'
        spawn_model_client(model_name=modelName,
               model_xml=open('/home/mdossantos/.gazebo/models/red_box/model.sdf', 'r').read(),
               robot_namespace=modelName, initial_pose=Pose(position, orient), reference_frame='world')

    else:

        modelName = 'blue_box'
        spawn_model_client(model_name=modelName,
            model_xml=open('/home/mdossantos/.gazebo/models/blue_box/model.sdf', 'r').read(),
            robot_namespace=modelName, initial_pose=Pose(position, orient), reference_frame='world')


    while (not rospy.is_shutdown()):
        pub.publish(str(sensor))




if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass