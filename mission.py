#!/bin/python3

import rclpy
import sys
import numpy as np
from time import sleep
import threading
from python_interface.drone_interface import DroneInterface
from as2_msgs.srv import SetSpeed
from as2_msgs.msg import TrajectoryWaypoints
import os

drone_id = "drone_0"


def drone_run(drone_interface):

    takeoff_height = 5.0
    takeoff_speed = 1.0
    dim = 10.0
    height = 5.0
    speed = 2.0
    
    print(f"Start mission {drone_id}")

    # drone_interface.offboard()
    # print("OFFBOARD")

    # drone_interface.arm()
    # print("ARMED")

    print(f"Take Off {drone_id}")
    # drone_interface.takeoff(takeoff_height, speed=1.0)
    # drone_interface.follow_path([[0.0, 0.0, takeoff_height]], speed=takeoff_speed)
    # drone_interface.send_motion_reference_pose([0.0, 0.0, 10.0])
    drone_interface.send_motion_reference_pose([0.0, 0.0, height])
    sleep(10.0)
    print(f"Take Off {drone_id} done")
    # drone_interface.send_motion_reference_pose([0.0, 0.0, takeoff_height])
    # sleep(4.0)
    # drone_interface.send_motion_reference_twist([0.0, 0.0, 1.0])

    # sleep(5.0)

    # drone_interface.follow_path([
    #     [50, 50, 2],
    #     [100, 100, 2]
    #     ], speed=speed)

    
    path = [
        [ dim,  dim, height],
        [ dim, -dim, height],
        [-dim,  dim, height],
        [-dim, -dim, height],
        [   0,    0, height]]

    # path = [
    #     [ dim, 0.0, height],
    #     [-dim, 0.0, height],
    #     [ dim, 0.0, height],
    #     [-dim, 0.0, height],
    #     [ 0.0, 0.0, height]]

    # global_path = []

    # for i in range(20):
    #     print(f"Send path {drone_id}")
    #     drone_interface.follow_path(path, speed=speed)
    #     sleep(10)
    #     print(f"Send path {drone_id} done")

    # for i in range(20):
    #     global_path = global_path + path

    # print(f"Send path {drone_id}")
    # drone_interface.follow_path(global_path, speed=speed)
    # print(f"Send path {drone_id} done")

    # sleep(5)
    for i in range(20):
        for wp in path:
            print(f"Go to {drone_id}: [{wp[0]},{wp[1]},{height}]")
            drone_interface.go_to_point(wp, speed=speed, ignore_yaw=True)
            print(f"Go to {drone_id} done")
            sleep(15.0)

    # sleep(1.0)
    # print(f"Follow path {drone_id}")
    # path = [goal0, goal1, [0, 0, height]]
    # drone_interface.follow_path(path, speed=speed)
    # print(f"Follow path {drone_id} done")

    # sleep(5.0)
    # print(f"Land {drone_id}")
    # drone_interface.land(speed=0.5)
    # print(f"Land {drone_id} done")

    print("Clean exit")


if __name__ == '__main__':
    rclpy.init()
    n_uavs = DroneInterface(drone_id, verbose=True)

    drone_run(n_uavs)

    n_uavs.shutdown()
    rclpy.shutdown()
    exit(0)
