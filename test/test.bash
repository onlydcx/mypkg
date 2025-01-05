#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"
cd $dir/ros2_ws

source $dir/.bashrc
timeout 10 ros2 run mypkg memory_node > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Memory Usage:'
