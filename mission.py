#!/bin/python3

from time import sleep
import rclpy
from python_interface.drone_interface import DroneInterface
from as2_msgs.msg import TrajectoryWaypoints

drone_id = "drone_sim_0"


def drone_run(drone_interface):

    loops = 5
    dim_x = 10.0
    dim_y = 4.0
    height = 2.0

    gates_path = [
        [    dim_x, -dim_y, height],
        [2.0*dim_x,   0.0,  height],
        [    dim_x,  dim_y, height],
        [      0.0,    0.0, height]]

    takeoff_height = 1.0
    takeoff_speed = 0.5
    speed = 5.0
    yaw_mode = TrajectoryWaypoints.PATH_FACING

    print(f"Start mission {drone_id}")

    drone_interface.offboard()
    print("OFFBOARD")

    drone_interface.arm()
    print("ARMED")

    print(f"Take Off {drone_id}")
    drone_interface.follow_path(
        [[0.0, 0.0, takeoff_height]], speed=takeoff_speed, yaw_mode=yaw_mode)
    print(f"Take Off {drone_id} done")

    sleep(1.0)

    for i in range(loops):
        print(f"Loop {i}")
        drone_interface.follow_path(
            gates_path,
            speed=speed,
            yaw_mode=yaw_mode)
        print(f"Loop {i} done")

    print("Clean exit")


if __name__ == '__main__':
    rclpy.init()
    n_uavs = DroneInterface(drone_id, verbose=False, use_sim_time=True)

    drone_run(n_uavs)

    n_uavs.shutdown()
    rclpy.shutdown()
    exit(0)
