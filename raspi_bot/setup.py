from setuptools import setup

package_name = 'raspi_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'pub_rpi_node=raspi_bot.publisher_node:main',
            'sub_rpi_node=raspi_bot.subsrciber_node:main',
        ],
    },
)
