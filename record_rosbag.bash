#!/bin/bash

DRONE_ID_NAMESPACE="drone_sim_dps_0"

mkdir rosbags 
cd rosbags &&\
ros2 bag record \
"/$DRONE_ID_NAMESPACE/self_localization/odom" \
"/$DRONE_ID_NAMESPACE/actuator_command/thrust" \
"/$DRONE_ID_NAMESPACE/actuator_command/twist" \
"/$DRONE_ID_NAMESPACE/motion_reference/trajectory" \
"/$DRONE_ID_NAMESPACE/test1" \
"/$DRONE_ID_NAMESPACE/test2" \
"/$DRONE_ID_NAMESPACE/test3" \
"/$DRONE_ID_NAMESPACE/test4" \
"/$DRONE_ID_NAMESPACE/debug/traj_generated"
#"/$DRONE_ID_NAMESPACE/image_raw" \
#"/$DRONE_ID_NAMESPACE/aruco_gate_detector/gate_img_topic" \
