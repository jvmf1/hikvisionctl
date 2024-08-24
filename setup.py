from setuptools import find_packages, setup

setup(
    name='hikvisionctl',
    version='0.1',
    author='jvmf1',
    license='LICENSE',
    install_requires=['xmltodict','requests'],
    scripts = ['hikvisionctl']
)
