from setuptools import setup, find_packages

setup(
    name="shared_definitions",
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pydantic==2.3.0',
    ],
)
