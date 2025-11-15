"""
the setup.py is an essential part of packaginh
and distributing python projects.
It is used by setuptools (or distutils)
to define configuration of your project"""



from setuptools import find_packages,setup
from typing import List
import os



def get_requirements()->List[str]:
    """this function return to requirements """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                 requirement=line.strip()
                 if requirement and requirement!='-e .':
                     requirement_list.append(requirement)



    except FileNotFoundError:
        print("requirements.txt file is not found")

    return requirement_list
print(get_requirements())


setup(
    name="Network_Security",
    version="0.0.1",
    author="bhaskar phaneendra",
    author_email="bhaskarphaneendra.t@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)