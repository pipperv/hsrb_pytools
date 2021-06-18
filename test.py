import math
import moveit_commander
import rospy
import tf
from utils import *

rospy.init_node("position_test")

drop_joint_array = [
    [0.2, -1.8, 0.0, 0.25, 0.0, 0],
    [0.0, -1.2, 0.0, -0.4, 0.0, 0]
]
#arm.set_joint_value_target([0, 0, 0.0, 0.0, 0.0, 0])
#arm.set_joint_value_target(drop_joint_array[0])
#rospy.loginfo(arm.go())

move_arm_neutral()

'''
Table Colission
wrench: 
  force: 
    x: -70.5522165832
    y: -17.2271613888
    z: 17.2428387995
  torque: 
    x: -0.624858048312
    y: 12.6063346139
    z: -1.87055298553
'''
'''
cero on joints
wrench: 
  force: 
    x: 0.767338743039
    y: -1.21425524663
    z: 11.1809071603
  torque: 
    x: 0.0895597174924
    y: 0.0046337575237
    z: 0.00987997693378
'''
'''
Init Pose
wrench: 
  force: 
    x: 10.9399639849
    y: 0.724610788475
    z: -1.08218417518
  torque: 
    x: -0.10414009385
    y: -0.346589601633
    z: 0.246784409436
'''
'''
Neutral Pose
wrench: 
  force: 
    x: 10.7274679831
    y: -1.69264707752
    z: -1.08798920068
  torque: 
    x: 0.215514307898
    y: -0.362866014775
    z: 0.163527174344
wrench: 
  force: 
    x: 11.0290293275
    y: 1.61761965609
    z: 0.838238454095
  torque: 
    x: -0.200827942958
    y: -0.341655749789
    z: -0.16891316756
'''
'''
Neutral Peach on Top
wrench: 
  force: 
    x: 11.1151805102
    y: -4.74528744461
    z: -1.63984004282
  torque: 
    x: 0.41038551644
    y: -0.405945396952
    z: 0.144810879457
'''