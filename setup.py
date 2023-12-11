from setuptools import setup, find_packages
from glob import glob

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='databot-py',
    version='0.0.7',
    packages=['databot'],
    include_package_data=True,
    package_data={
        'media': glob('media/*'),
        'data': glob('data/*'),
        'web': glob('web/*')
    },
    url='https://github.com/dbaldwin/databot-py',
    license='MIT',
    author='Pat Ryan, Dennis Baldwin',
    author_email='theyoungsoul@gmail.com, db@droneblocks.io',
    description='databot Python Library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'bleak==0.19.5'
    ]
)