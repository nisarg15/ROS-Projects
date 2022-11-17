#!/usr/bin/env python

# ENMM662 Introduction to Robot Modeling
# Fall 2022
# Professor Reza Monfaredi
# Author: Doug Summerlin and Nisarg Upadhyay
# UID: 114760753 and 118221625
# Project 1 Simple Subscriber
# run as: straight_line_subscriber.py

import rospy
from std_msgs.msg import Float64

def callback(vels):
    print("Commanded Velcocities Recieved by Subscriber: ")
    print(vels)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('straight_line_listener', anonymous=True)
   
    rospy.Subscriber('/project1_car_v4/right_steering_ctrl/command', Float64, callback, queue_size=10)
    rospy.Subscriber('/project1_car_v4/left_steering_ctrl/command', Float64, callback, queue_size=10)
    rospy.Subscriber('/project1_car_v4/right_drive_wheel_ctrl/command', Float64, callback, queue_size=10)
    rospy.Subscriber('/project1_car_v4/left_drive_wheel_ctrl/command', Float64, callback, queue_size=10)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()