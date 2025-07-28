
from setuptools import find_packages, setup
from typing import List

# to install packages and all stuff that are mentioned !

def get_requirements(file_path:str)-> List[str]:
    """This Function will return the list of functions"""

    requirements = []
    with open(file_path) as file_objects:
        requirements = file_objects.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        # to remove "-e .", coz it will identify it as package to install
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name = 'DataScience',
    version= '0.0.1',
    author= "Jatin",
    author_email= "ljatinl.reddy@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
