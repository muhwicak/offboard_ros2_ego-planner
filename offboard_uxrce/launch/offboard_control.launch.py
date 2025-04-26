#!/usr/bin/env python3
############################################################################
#
#   Copyright (C) 2022 PX4 Development Team. All rights reserved.
#   Modified for offboard_uxrce
#
############################################################################

__author__ = "Braden Wagstaff (Modified)"
__contact__ = "braden@arkelectron.com"

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    package_dir = get_package_share_directory('offboard_uxrce')
    
    return LaunchDescription([
        # Optional: Execute a bash script (uncomment if needed)
        # ExecuteProcess(
        #     cmd=['bash', os.path.join(package_dir, 'scripts', 'TerminatorScript.sh')],
        #     output='screen'
        # ),
        
        Node(
            package='offboard_uxrce',
            namespace='offboard_uxrce',
            executable='visualizer',
            name='visualizer',
            output='screen'
        ),
        Node(
            package='offboard_uxrce',
            namespace='offboard_uxrce',
            executable='processes',
            name='processes',
            prefix='gnome-terminal --',  # Optional: open in new terminal
            output='screen'
        ),
        Node(
            package='offboard_uxrce',
            namespace='offboard_uxrce',
            executable='Keyboard_control',
            name='Keyboard_control',
            prefix='gnome-terminal --',  # Optional: open in new terminal
            output='screen'
        ),
        Node(
            package='offboard_uxrce',
            namespace='offboard_uxrce',
            executable='Offboard_control',
            name='Offboard_control',
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', os.path.join(package_dir, 'visualize.rviz')],
            output='screen'
        )
    ])
