# responsible in creating the ML project as a package and can be deployed in Pypi

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # readlines will read the \n as well so we replace it with blank space 
        requirements = [req.replace("\n","") for req in requirements]
        
        # when we run requirements.txt we want it to to run setup,py 
        # but when setup.py is running we need not want it to come in this get_requirements function
        # removing -e . from requirements.txt since it will install the setup.py
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements




setup(
    # like a metadata of the project,constant information
    name = 'mlproject',
    version = '0.0.1',
    author = 'Dheepthi Reddy',
    author_email = 'dheepthireddyv@gmail.com',
    packages = find_packages(),
    # install_requires = ['pandas', 'numpy', 'seaborn']
    install_requires = get_requirements('requirements.txt')

)