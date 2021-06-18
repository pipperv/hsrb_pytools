import rospy
import numpy as np
import tf
from tf.transformations import quaternion_from_matrix
from geometry_msgs.msg import WrenchStamped
import std_msgs.msg as std
import tf2_geometry_msgs

class WrenchPub():
    def __init__(self):
        self.echo = rospy.Publisher("/wrench/listener", WrenchStamped, queue_size=1)
        self.grasp_detect = rospy.Publisher("/wrench/detection", std.Bool, queue_size=1)
    def listener(self):
        msg = rospy.wait_for_message("/hsrb/wrist_wrench/raw",  WrenchStamped)
        self.echo.publish(msg)
    def detection(self):
        wrench_raw = rospy.wait_for_message("/hsrb/wrist_wrench/raw",  WrenchStamped)
        torque = np.abs(wrench_raw.wrench.torque.x)
        if torque > 0.25:
            self.grasp_detect.publish(True)
        else:
            self.grasp_detect.publish(False)

rospy.init_node('wrench_listener')
w = WrenchPub()
while not rospy.is_shutdown():
    w.detection()