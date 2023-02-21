#!/bin/python3

import os
from time import sleep
import rclpy
from as2_python_api.drone_interface_gps import DroneInterfaceGPS
from as2_msgs.msg import YawMode
from geographic_msgs.msg import GeoPath


def drone_run(drone_interface: DroneInterfaceGPS):
    # ##### ARM OFFBOARD #####
    drone_interface.offboard()
    drone_interface.arm()

    # ##### TAKEOFF #####
    drone_interface.takeoff(2.0)

    ##### FOLLOW PATH #####
    path = [[40.44105500048261, -3.6888145000049426, 2.0], [40.4411080115872, -3.6887864023496664, 2.0], [40.44108352873846, -3.6886960545411274, 2.0], [40.44108300049554, -3.6887847170711674, 2.0], [40.4410585086582, -3.6886958777954137, 2.0], [40.441056467299525, -3.688672408466516, 2.0]]
    drone_interface.follow_path(path, 1.0)

    ##### LAND #####
    drone_interface.land()


if __name__ == '__main__':
    rclpy.init()
    # Get environment variable AEROSTACK2_SIMULATION_DRONE_ID
    # uav_name = os.environ.get("AEROSTACK2_SIMULATION_DRONE_ID")
    uav = DroneInterfaceGPS("drone_sim_rafa_0", verbose=True, use_sim_time=True)

    drone_run(uav)

    uav.shutdown()
    rclpy.shutdown()

    print("Clean exit")
    exit(0)
