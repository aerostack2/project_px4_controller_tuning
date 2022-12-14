#!/bin/bash

AEROSTACK_PROJECT=$(pwd)
SCRIPT_PATH="${AEROSTACK2_PATH}/simulation/gazebo_assets/scripts"
GAZEBO_ASSETS="${AEROSTACK2_PATH}/simulation/gazebo_assets"

GAZEBO_MODEL_PATH="$GAZEBO_ASSETS/configs/gazebo/models"
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$MODEL_FOLDER
WORLD_FOLDER="$GAZEBO_ASSETS/worlds"
export GAZEBO_RESOURCE_PATH=$GAZEBO_ASSETS:$WORLD_FOLDER

$SCRIPT_PATH/default_run.sh "${AEROSTACK_PROJECT}/simulation_config/default.json"
