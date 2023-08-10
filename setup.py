from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return list of requirements 
    '''
    requirements = []
    HYPEN_DOT = '-e.'
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='shafaq',
    author_email='shafaqrana2@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('Requirement.txt')
)

 
