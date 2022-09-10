#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="src",
    version="0.0.1",
    description="session2 assignment for pytorch lightening with hydra, docker",
    author="manju kiran",
    author_email="manjukiran66@gmail.com",
    url="https://github.com/user/Manjukiran66/emlv2_session02",  # REPLACE WITH YOUR OWN GITHUB PROJECT LINK
    install_requires=["pytorch-lightning", "hydra-core"],
    packages=find_packages(),
)
