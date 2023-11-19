from setuptools import setup, find_packages

setup(
    name='puppet_master',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A high-level Ansible Python project for Oracle database operations',
    packages=find_packages(),
    install_requires=[
        'cx_Oracle',
        'ansible'
        # Add any other dependencies here
    ],
)
