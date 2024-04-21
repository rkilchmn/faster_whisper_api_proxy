# setup.py

from setuptools import setup

setup(
    name='faster_whisper_api_proxy',  # Name of your module
    version='1.0.0',    # Version number
    description='a python module that is a drop in replacement for faster_whisper but calls a remote faster_whisper implementation via API',
    packages=['faster_whisper_api_proxy'],  # List of packages to include
    install_requires=[
        'typing',
        'numpy',
        'requests',
        'json',
        'collections',
        'urllib'
    ],      # List of dependencies
)
