#!/bin/python3

import os
from time import sleep
import rclpy
from python_interface.drone_interface import DroneInterface
from as2_msgs.msg import YawMode


def drone_run(drone_interface: DroneInterface):

    speed = 1.5
    takeoff_height = 1.0
    height = 3.0

    sleep_time = 2.0
    yaw_mode = YawMode()
    yaw_mode.mode = YawMode.PATH_FACING

    dim = 3.0
    path = [
        [dim, dim, height],
        [dim, -dim, height],
        [-dim, dim, height],
        [-dim, -dim, height],
        [0.0, 0.0, takeoff_height],
    ]

    print("Start mission")

    ##### ARM OFFBOARD #####
    drone_interface.offboard()
    drone_interface.arm()

    ##### TAKE OFF #####
    print("Take Off")
    drone_interface.takeoff(takeoff_height, speed=1.0)
    print("Take Off done")
    sleep(sleep_time)

    ##### FOLLOW PATH #####
    sleep(sleep_time)
    print(f"Follow path: [{path}]")
    drone_interface.follow_path.follow_path_with_path_facing(path, speed)
    print("Follow path done")

    ##### GOTO #####
    for goal in path:
        print(f"Go to {goal}")
        drone_interface.goto.go_to_point_path_facing(goal, speed=speed)
        print("Go to done")
        sleep(sleep_time)

    ##### LAND #####
    print("Landing")
    drone_interface.land(speed=0.5)
    print("Land done")

    drone_interface.disarm()


if __name__ == '__main__':
    rclpy.init()
    # Get environment variable AEROSTACK2_SIMULATION_DRONE_ID
    uav_name = os.environ['AEROSTACK2_SIMULATION_DRONE_ID']
    uav = DroneInterface(uav_name, verbose=True, use_sim_time=True)

    drone_run(uav)

    uav.shutdown()
    rclpy.shutdown()

    print("Clean exit")
    exit(0)
