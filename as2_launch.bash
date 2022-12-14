#!/bin/bash

UAV_MASS=0.82
UAV_MAX_THRUST=16.7

if [ "$#" -le 0 ]; then
	echo "usage: $0 [drone_namespace] "
	exit 1
fi

# Arguments
drone_namespace=$1
use_sim_time=true
controller="SP"
behavior_type="position"

if [[ "$controller" == "DF" ]]
then
    behavior_type="trajectory"
fi

source ./utils/launch_tools.bash

new_session $drone_namespace
new_window 'RTPS interface' "micrortps_agent -t UDP -n $drone_namespace"

new_window 'pixhawk interface' "ros2 launch pixhawk_platform pixhawk_platform_launch.py \
    namespace:=$drone_namespace \
    config:=config/platform_default.yaml \
    simulation_mode:=true \
    use_sim_time:=$use_sim_time"

new_window 'controller_manager' "ros2 launch controller_manager controller_manager_launch.py \
    namespace:=$drone_namespace \
    use_bypass:=true \
    config:=config/$controller/controller.yaml \
    use_sim_time:=$use_sim_time"

new_window 'state_estimator' "ros2 launch basic_state_estimator basic_state_estimator_launch.py \
    namespace:=$drone_namespace \
    odom_only:=true \
    use_sim_time:=$use_sim_time" 

new_window 'basic_behaviours' "ros2 launch as2_basic_behaviors all_basic_behaviors_launch.py \
    namespace:=$drone_namespace \
    config_takeoff:=config/$behavior_type/takeoff_behaviour.yaml \
    config_goto:=config/$behavior_type/goto_behaviour.yaml \
    config_follow_path:=config/$behavior_type/follow_path_behaviour.yaml \
    config_land:=config/land_behaviour.yaml \
    use_sim_time:=$use_sim_time"

if [[ "$behavior_type" == "trajectory" ]]
then
    new_window 'traj_generator' "ros2 launch trajectory_generator trajectory_generator_launch.py  \
        namespace:=$drone_namespace \
        use_sim_time:=$use_sim_time"
fi