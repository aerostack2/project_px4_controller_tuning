#!/bin/bash

drone_namespace=${AEROSTACK2_SIMULATION_DRONE_ID::-1}

tmux ls | grep -Po "${drone_namespace}\d+" | xargs -I % sh -c 'tmux kill-session -t %'

pkill -9 python
pkill -9 python3
