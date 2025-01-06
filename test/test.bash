#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"


cd $dir/ros2_ws
colcon build
source $dir/.bashrc
# timeout 10 ros2 run mypkg memory_node > /tmp/mypkg.log
timeout 10 ros2 launch mypkg memory_publisher.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Memory Usage:'
