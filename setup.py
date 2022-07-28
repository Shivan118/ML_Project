from setuptools import setup, find_packages
from typing import List

# Decelarding Variables for setup functions

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.3"
AUTHOR = "Shivan Kumar"
DESCRIPTION = "This is  a first ML Project"
REQUIREMENT_FILE_NAME ="requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Descritpion: This function is goging to return list of 
    requirement mention in requirements.txt file

    return This function is goging to return a list which contain 
    name of libraries mentioned in reqquriments.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove('-e .')


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR, 
    description = DESCRIPTION, 
    packages=find_packages(), 
    install_requires=get_requirements_list()
    )

    