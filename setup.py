from gettext import install
from setuptools import setup
from typing import List

# Decelarding Variables for setup functions

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = " SHIVAN KUMAR"
DESCRIPTION = "This is  a first ML Project"
PACKAGES = ['housing']
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Descritpion: This function is goging to return list of 
    requirement mention in requirements.txt file

    return This function is goging to return a list which contain 
    name of libraries mentioned in reqquriments.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR, 
description = DESCRIPTION, 
packages = PACKAGES,
install_requires = get_requirements_list()

)


if __name__=="__main__":
    print(get_requirements_list())