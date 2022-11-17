READ ME

# ========================================
# ENPM662 Fall 2022: Introduction to Robotic Modeling
# Project #1
#
# Author: Nisarg Upadhyay (dsumm1001@gmail.com) and Nisarg Upadhyay (nisarg15@umd.edu)
# UID: 114760753(Doug) and 118221625(Nisarg)
# Directory ID: dsummerl and nisarg15
# =========================================

FILESYSTEMS: cd into the folder titled "nisarg15_project1" after extracting it from the zip file on an Ubunutu operating system. Insert the package "project1_car_v4" into your catkin_ws. The only external library that may not be present for the user would be the python "time" library used in the straight line publisher node. 

OPERATING SYSTEM: Linux Ubuntu 20.04 via Dual Boot

FIRST RUN                   $ catkin_make clean && catkin_make
NEXT RUN                    $ source ~/<your_catkin_ws>/devel/setup.bash
TO RUN ROS LAUNCH FILES     $ cd ~/home/.../<your_catkin_ws>
TO RUN PYTHON SCRIPTS:      $ cd ~/home/.../<your_catkin_ws>/project1_car_v4/src

CAR TELEOP:                 $ roslaunch project1_car_v4 final_launch.launch
    (in separate terminal)  $ python3 teleop_template.py
The launch file will spawn the robot with mounted LIDAR in the gazebo arena at the map origin point. Then in a separate terminal, cd into the /src/ folder and run the python command above. This will prompt the user for terminal inputs in order to make the robot move. Best results for movement involved holding the "w" key until a sufficiently large max linear volume was achieved an then using the "m", ",", and "." keys to turn right, move straight, and turn left respectively. Other commands for bot movement are printed to the terminal. 


STRAIGHT LINE SUB/PUB:      $ roslaunch project1_car_v4 subpub_launch.launch
    (in separate terminal)  $ python3 straight_line_subscriber.py
    (in separate terminal)  $ python3 straight_line_publisher.py
The launch file will spawn the robot with mounted LIDAR in the empty gazebo world at the map origin point. Then in a separate terminal, cd into the /src/ folder and run the first python command above. This will start the subscriber node that reads and prints the data published to the joint controller topics. After that, in a separate terminal, cd into the /src/ folder and run the second python command above. This will run a script that publishes an increasing velocity to the rear wheel velocity control topics for 20 seconds, and then ring the car to a sudden halt. The publisher will print the publishes velocities to the terminal. After that the publisher node will die. 