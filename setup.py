from setuptools import setup, find_packages

setup(
    name='asv_tester',
    version='0.1.0',
    packages=find_packages(include=['asv_tester', 'asv_tester.*'])
)