import os
from glob import glob
from setuptools import setup, find_packages

package_name = 'offboard_uxrce'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('share', package_name), glob('resource/*.rviz')),
        # (os.path.join('share', package_name, 'scripts'), glob('scripts/*.sh'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='muhammadwicak97@gmail.com',
    description='Offboard UXRCE Control Package',
    license='Apache License 2.0',  # (or choose your actual license)
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'offboard_control = offboard_uxrce.offboard_control:main',
            'visualizer = offboard_uxrce.visualizer:main',
            'velocity_control = offboard_uxrce.velocity_control:main',
            'control = offboard_uxrce.control:main',
            'processes = offboard_uxrce.processes:main'
        ],
    },
)
