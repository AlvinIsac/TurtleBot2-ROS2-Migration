import os

import ament_index_python.packages
import launch
import launch_ros.actions

import yaml


def generate_launch_description():
    share_dir = ament_index_python.packages.get_package_share_directory('kobuki_node')
    params_file = os.path.join(share_dir, 'config', 'kobuki_node_params.yaml')
    
    with open(params_file, 'r') as f:
        params = yaml.safe_load(f)['kobuki_ros_node']['ros__parameters']
    
    kobuki_ros_node = launch_ros.actions.Node(
        package='kobuki_node',
        executable='kobuki_ros_node',
        output='both',
        parameters=[params],
        remappings=[
            ('commands/velocity', 'cmd_vel'),
            ('commands/led1', 'cmd/led1'),
            ('commands/led2', 'cmd/led2'),
            ('commands/digital_output', 'cmd/digital_output'),
            ('commands/external_power', 'cmd/external_power'),
            ('commands/sound', 'cmd/sound'),
            ('commands/reset_odometry', 'cmd/reset_odometry'),
            ('commands/motor_power', 'cmd/motor_power'),
            ('commands/controller_info', 'cmd/controller_info'),
        ]
    )

    urg_node_driver = launch_ros.actions.Node(
        package='urg_node',
        executable='urg_node_driver',
        output='screen',
        arguments=['--ros-args', '-p', 'serial_port:=/dev/ttyACM0']
    )

    return launch.LaunchDescription([kobuki_ros_node, urg_node_driver])
