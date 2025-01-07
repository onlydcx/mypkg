# SPDX-FileCopyrightText: 2025 Rin Hanaoka <s23c1110vk@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    memory_publisher = launch_ros.actions.Node(
        package='mypkg',
        executable='memory_publisher',
    )

    return launch.LaunchDescription([memory_publisher])
