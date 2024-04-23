# setup.py

from setuptools import setup, find_packages

setup(
    name='faster_whisper_api_proxy',  # Name of your module
    version='1.0.1',    # Version number
    description='a python module that is a drop in replacement for faster_whisper but calls a remote faster_whisper implementation via API',
    packages=find_packages(include=['faster_whisper_api_proxy', 'faster_whisper_api_proxy.*'], 
    url='https://github.com/rkilchmn/faster_whisper_api_proxy',
    author='Roger Kilchenmann',
    author_email='roger@kilchenmann.net',
    keywords=['AI','faster_whisper','transcribe','natural language','speech recognition','api','remote'],
    install_requires=[
        'numpy',
        'requests'
    ],     
)
