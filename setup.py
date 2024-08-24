from setuptools import find_packages, setup

setup(
    name='hikvision-config',
    version='0.1',
    author='jvmf1',
    license='LICENSE',
    packages=find_packages(),
    scripts = ['hikvisionctl']
)
