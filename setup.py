from setuptools import setup

setup(
    name='snapshotalyzer',
    version='0.1',
    author='Graham Cole',
    author_email='grahamcole23@gmail.com',
    description='SnapshotAlyzer is a tool to manage AWS EC2 snapshots',
    licence='MIT',
    packages=['shotty'],
    url="https://github.com/spydersweb/aws_ec2_py",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)