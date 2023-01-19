#!/bin/bash

export PX4_HOME_LAT=40.158194
export PX4_HOME_LON=-3.380795
export PX4_HOME_ALT=100

AEROSTACK_PROJECT=$(pwd)
$AS2_GZ_ASSETS_SCRIPT_PATH/default_run.sh "${AEROSTACK_PROJECT}/simulation_config/gates.json"