from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MUSIC COMPOSER",
    version="6.9",
    author="Morshed",
    packages=find_packages(),
    install_requires = requirements,
)