#!/bin/python3

from time import sleep
import rclpy
from python_interface.drone_interface import DroneInterface
from as2_msgs.msg import TrajectoryWaypoints

from motion_reference_handlers.hover_motion import HoverMotion

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

    takeoff_height = 2.5
    takeoff_speed = 0.5
    speed = 4.0
    yaw_mode = TrajectoryWaypoints.PATH_FACING

    print(f"Start mission {drone_id}")

    drone_interface.offboard()
    print("OFFBOARD")

    drone_interface.arm()
    print("ARMED")

    sleep(1.0)

    print(f"Take Off {drone_id}")
    drone_interface.follow_path(
        [[0.5, 0.0, takeoff_height*0.5], [1.0, 0.0, takeoff_height]], speed=takeoff_speed, yaw_mode=yaw_mode)
    print(f"Take Off {drone_id} done")

    # sleep(10.0)
    
    # print("Send hover")
    # hover_motion_handler = HoverMotion(drone_interface)
    # hover_motion_handler.send_hover()
    # print("Send hover done")

    # return
    
    # for i in range(loops):
    #     print(f"Loop {i}")
    #     drone_interface.follow_path(
    #         gates_path,
    #         speed=speed,
    #         yaw_mode=yaw_mode)
    #     print(f"Loop {i} done")
        
    path_to_send = []
    for i in range(loops):
        path_to_send += gates_path
        
    print(f"Loop {i}")
    drone_interface.follow_path(
        path_to_send,
        speed=speed,
        yaw_mode=yaw_mode)
    print(f"Loop {i} done")
    
    sleep(15.0)
    
    print("Send hover")
    hover_motion_handler = HoverMotion(drone_interface)
    hover_motion_handler.send_hover()
    print("Send hover done")

    print("Clean exit")


if __name__ == '__main__':
    rclpy.init()
    n_uavs = DroneInterface(drone_id, verbose=False, use_sim_time=True)

    drone_run(n_uavs)

    n_uavs.shutdown()
    rclpy.shutdown()
    exit(0)
