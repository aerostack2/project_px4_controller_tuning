#!/bin/bash

if [ "$#" -le 0 ]; then
	echo "usage: $0 [drone_namespace] "
	exit 1
fi

# Arguments
drone_namespace=$1
use_sim_time=true
controller="speed_controller" # "differential_flatness" or "speed_controller"
behavior_type="position"

if [[ "$controller" == "differential_flatness" ]]
then
    behavior_type="trajectory"
fi

source ./utils/launch_tools.bash

new_session $drone_namespace

new_window 'RTPS interface' "micrortps_agent -t UDP -n $drone_namespace"

new_window 'platform' "ros2 launch as2_platform_pixhawk pixhawk_launch.py \
    namespace:=$drone_namespace \
    use_sim_time:=$use_sim_time \
    config:=config/platform_default.yaml"

new_window 'controller' "ros2 launch as2_controller controller_launch.py \
    namespace:=$drone_namespace \
    use_sim_time:=$use_sim_time \
    cmd_freq:=100.0 \
    info_freq:=10.0 \
    use_bypass:=true \
    plugin_name:=${controller} \
    plugin_config_file:=config/${controller}_controller.yaml"

new_window 'state_estimator' "ros2 launch as2_state_estimator state_estimator_launch.py \
    namespace:=$drone_namespace \
    use_sim_time:=$use_sim_time \
    plugin_name:=external_odom"

new_window 'behaviors' "ros2 launch as2_behaviors_motion motion_behaviors_launch.py \
    namespace:=$drone_namespace \
    use_sim_time:=$use_sim_time \
    follow_path_plugin_name:=follow_path_plugin_$behavior_type \
    goto_plugin_name:=goto_plugin_$behavior_type \
    takeoff_plugin_name:=takeoff_plugin_$behavior_type \
    land_plugin_name:=land_plugin_speed"

if [[ "$behavior_type" == "trajectory" ]]
then
    new_window 'traj_generator' "ros2 launch as2_behaviors_trajectory_generator dynamic_polynomial_generator_launch.py  \
        namespace:=$drone_namespace \
        use_sim_time:=$use_sim_time"
fi