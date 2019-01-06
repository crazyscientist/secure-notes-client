#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name='securenotes-client',
    version='0.2.0',
    author="Andreas Hasenkopf",
    author_email="andreas@hasenkopf.xyz",
    description="Command line client for SecureNotes",
    url="https://github.com/crazyscientist/secure-notes-client",
    packages=find_packages(),
    python_requires=">=3.5",
    scripts=["securenotes.py",],
    install_requires=['requests', 'pycryptodomex', 'mdv']
)