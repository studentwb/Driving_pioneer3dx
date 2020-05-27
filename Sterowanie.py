import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Transform
from geometry_msgs.msg import Vector3
import time

twist = 0;
"""
Program ma na celu jeżdżenie po kwadracie robota Pioneer 3DX
"""

def start():
    global pub
    pub = rospy.Publisher('/pioneer_1/RosAria/cmd_vel', Twist, queue_size=10)
    rospy.init_node('vel_controller', anonymous=True)


def set_vel(v, w):
    global twist
    global pub
    twist = Twist()
    twist.linear.x = v
    twist.linear.y = v
    twist.linear.z = v
    twist.angular.z = w
    print
    twist
    pub.publish(twist)
    

if __name__ == '__main__':
    start()
    set_vel(0.0, 0.0)
    rospy.sleep(1)
    set_vel(0.3, 0.0)
    rospy.sleep(6)
    for i in range(4):
        set_vel(0.3, 0.0)
        rospy.sleep(6)
        set_vel(0.3, -0.94)
        rospy.sleep(1)
    set_vel(0.0, 0.0)