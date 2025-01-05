from setuptools import find_packages, setup
import os
import glob

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob.glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Rin Hanaoka',
    maintainer_email='s23c1110vk@s.chibakoudai.jp',
    description='a package for ROS2 practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 'talker = mypkg.talker:main',
            # 'listener = mypkg.listener:main',
            'memory_node = mypkg.memory_publisher:main',
        ],
    },
)
