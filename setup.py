from setuptools import find_packages, setup

package_name = 'cpts483'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sihui',
    maintainer_email='sihui@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = cpts483.my_node:main',
            'service = cpts483.talker:main',
            'client = cpts483.asker:main',
        ],
    },
)
