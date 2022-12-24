
from setuptools import setup

setup(
    name='hello-world',
    version='0.1.0',
    description='A Python package that says "Hello, world!"',
    author='Your Name',
    author_email='your@email.com',
    packages=['hello_world'],
    entry_points={
        'console_scripts': [
            'hello-world=hello_world.__main__:main'
        ]
    }
)
