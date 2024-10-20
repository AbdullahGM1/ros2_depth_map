from setuptools import find_packages, setup

package_name = 'ros2_depth_map'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='AbdullagGM',
    maintainer_email='agm.musalami@gmail.com',
    description='Converting Point Cloud Points to a Depth Map',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'depth_map = ros2_depth_map.depth_map:main'
        ],
    },
)
