from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path)->List[str]:
    requiremnets=[]
    with open(file_path) as file_obj:
        requiremnets = file_obj.readlines()
        requiremnets = [req.replace("\n"," ") for req in requiremnets]
    if HYPEN_E_DOT in requiremnets:
        requiremnets.remove(HYPEN_E_DOT)

    return requiremnets  

setup(
    name = 'MLOPS',
    version = '0.0.1',
    author = 'Naman',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt') 
)