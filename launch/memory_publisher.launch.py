import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    memory_publisher = launch_ros.actions.Node(
        package='mypkg',
        executable='memory_node',
    )

    return launch.LaunchDescription([memory_publisher])
