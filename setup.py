# setup.py
from setuptools import setup, find_packages

setup(
    name="quantum-computing-cacic2025",
    version="0.1.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
)
