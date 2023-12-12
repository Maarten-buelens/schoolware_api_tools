from setuptools import find_packages, setup
setup(
    name='schoolware_api_tools',
    packages=find_packages(include=['schoolware_api_tools']),
    version='0.0.0',
    description='some tools for schoolware api made in python',
    author='Maarten Buelens',
    install_requires=['schoolware_api'],
    author_email='schoolware_api@mb-server.com',
)