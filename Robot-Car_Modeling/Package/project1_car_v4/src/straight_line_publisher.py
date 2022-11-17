#!/usr/bin/env python

# ENMM662 Introduction to Robot Modeling
# Fall 2022
# Professor Reza Monfaredi
# Author: Doug Summerlin and Nisarg Upadhyay
# UID: 114760753 and 118221625
# Project 1 Simple Publisher
# run as: straight_line_publisher.py


import rospy
import time
from std_msgs.msg import Float64

def straight_talker():
    pub_right = rospy.Publisher('/project1_car_v4/right_steering_ctrl/command', Float64, queue_size=10)
    pub_left = rospy.Publisher('/project1_car_v4/left_steering_ctrl/command', Float64, queue_size=10)
    pub_drive_right = rospy.Publisher('/project1_car_v4/right_drive_wheel_ctrl/command', Float64, queue_size=10)
    pub_drive_left = rospy.Publisher('/project1_car_v4/left_drive_wheel_ctrl/command', Float64, queue_size=10) 
    rospy.init_node('straight_line_pub', anonymous=True)
    rate = rospy.Rate(50) # 50hz
    
    while not rospy.is_shutdown():
        print("Commanding Velocity")
        for i in range(20):
            pub_right.publish(0.0)
            pub_left.publish(0.0)
            pub_drive_right.publish(-i)
            pub_drive_left.publish(-i)
            print("Steering Velocity: 0")
            print("Steering Velocity: ", -i)
            time.sleep(1)
            rate.sleep()
        
        pub_right.publish(0.0)
        pub_left.publish(0.0)
        pub_drive_right.publish(0.0)
        pub_drive_left.publish(0.0)
        rate.sleep()

        break

if __name__ == '__main__':
    try:
        straight_talker()
    except rospy.ROSInterruptException:
        pass