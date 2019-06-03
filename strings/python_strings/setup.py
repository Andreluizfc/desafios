import os

from setuptools import find_packages
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


requirements = read("requirements.txt").split()


setup
(
    name="python_strings",
    version="2.0",
    author="Andre Castro",
    author_email="andreluizfc1@gmail.com",
    description=("A library for strings formatting"),
    packages=find_packages(exclude=["docs", "files"]),
    include_package_data=True,
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/Andreluizfc/desafios/tree/master/strings",
    install_requires=requirements,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    classifiers=["Programming Language :: Python :: 3", "Operating System :: OS Independent"],
)
