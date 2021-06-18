import rospy
from geometry_msgs.msg import WrenchStamped
import math
import numpy as np
import moveit_commander
import tf
from utils import *

rospy.init_node("drop")
wrench_raw = rospy.wait_for_message("/hsrb/wrist_wrench/raw",  WrenchStamped)
init_torque = wrench_raw.wrench.torque.y
torque_offset = 0.1
init_height = 0.45
init_joints = [init_height, -2.1, 0.0, 0.4, 0.0, 0]
arm.set_joint_value_target(init_joints)
rospy.loginfo(arm.go())
actual_height = init_height
height_step = 0.005
while not rospy.is_shutdown():
    actual_height = actual_height - height_step
    init_joints = [actual_height, -2.1, 0.0, 0.4, 0.0, 0]
    arm.set_joint_value_target(init_joints)
    arm.go()
    wrench_raw = rospy.wait_for_message("/hsrb/wrist_wrench/raw",  WrenchStamped)
    if np.abs(wrench_raw.wrench.torque.y) > np.abs(init_torque) + torque_offset:
        move_hand(0.8)
        move_arm_neutral()
        move_hand(0.0)
        break
    