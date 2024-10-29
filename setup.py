from setuptools import setup, find_packages

def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

requirements = read_requirements("requirements.txt")

setup(
    name = 'test_repo',
    version = "1.0",
    description = 'A simple example python package.',
    install_requires = requirements
)
