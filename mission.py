#!/bin/python3

import os
from time import sleep
import rclpy
from as2_python_api.drone_interface_gps import DroneInterfaceGPS
from as2_msgs.msg import YawMode
from geographic_msgs.msg import GeoPath


def drone_run(drone_interface: DroneInterfaceGPS):

    speed = 2.0
    takeoff_height = 1.0
    height = 2.0

    sleep_time = 2.0
    yaw_mode = YawMode()
    yaw_mode.mode = YawMode.PATH_FACING

    dim = 0.000001
    path = [
        [47.3977419, 8.5455933, height],
        [47.3977419, 8.5455933 + dim, height],
        [47.3977419 + dim, 8.5455933 + dim, height],
        [47.3977419 + dim, 8.5455933, height],
        [47.3977419, 8.5455933, height]
    ]

    print("Start mission")
    
    drone_interface.gps.set_origin([47.3977419, 8.5455933, 0.0])

    ##### ARM OFFBOARD #####
    drone_interface.offboard()
    drone_interface.arm()

    ##### TAKE OFF #####
    print("Take Off")
    drone_interface.takeoff(takeoff_height, speed=1.0)
    print("Take Off done")
    sleep(sleep_time)

    ##### FOLLOW PATH #####
    # sleep(sleep_time)
    # print(f"Follow path with path facing: [{path}]")
    # drone_interface.follow_path()
    # print("Follow path done")

    # ##### GOTO #####
    for goal in path:
        print(f"Go to with path facing {goal}")
        drone_interface.goto.go_to_gps_point(goal, speed)
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
    uav_name = os.environ.get("AEROSTACK2_SIMULATION_DRONE_ID")
    uav = DroneInterfaceGPS(uav_name, verbose=False, use_sim_time=True)

    drone_run(uav)

    uav.shutdown()
    rclpy.shutdown()

    print("Clean exit")
    exit(0)
