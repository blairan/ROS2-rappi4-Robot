from setuptools import setup
import os
from glob import glob

package_name = 'raspi_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
        (os.path.join('share', package_name, 'qr_code_world'), glob('qr_code_world/*')),
        

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='blairan',
    maintainer_email='blairan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub_node=raspi_bot.publisher_node:main',
            'sub_node=raspi_bot.subsrciber_node:main',
            'qr_maze_node=raspi_bot.qr_maze_drive:main',
        ],
    },
)
