#!/bin/bash

UAV_MASS=0.82
UAV_MAX_THRUST=16.7

if [ "$#" -le 0 ]; then
	echo "usage: $0 [drone_namespace] "
	exit 1
fi

# Arguments
drone_namespace=$1

source ./launch_tools.bash

new_session $drone_namespace

new_window 'controller_manager' "ros2 launch controller_manager controller_manager_launch.py \
    drone_id:=$drone_namespace \
    use_bypass:=true \
    config:=config/SP/controller.yaml \
    use_sim_time:=true"

new_window 'RTPS interface' "micrortps_agent -t UDP -n $drone_namespace"

new_window 'pixhawk interface' "ros2 launch pixhawk_platform pixhawk_platform_launch.py \
    drone_id:=$drone_namespace \
    config:=config/SP/platform_default.yaml \
    simulation_mode:=true \
    use_sim_time:=true"

new_window 'state_estimator' "ros2 launch basic_state_estimator basic_state_estimator_launch.py \
    drone_id:=$drone_namespace \
    odom_only:=true \
    base_frame:='\"\"'  \
    use_sim_time:=true" 

new_window 'basic_behaviours' "ros2 launch as2_basic_behaviours all_basic_behaviours_launch.py \
    drone_id:=$drone_namespace \
    config_follow_path:=config/SP/follow_path_behaviour.yaml \
    config_takeoff:=config/SP/takeoff_behaviour.yaml \
    config_land:=config/SP/land_behaviour.yaml \
    config_goto:=config/SP/goto_behaviour.yaml \
    use_sim_time:=true"

new_window 'trajectory_generator' "ros2 launch trajectory_generator trajectory_generator_launch.py  \
    drone_id:=$drone_namespace "
