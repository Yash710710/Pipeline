from setuptools import setup, find_packages

from typing import List
def get_requirements(file_path: str) -> List[str]:
    '''
    this function returns the list of requirements so that get_requirements reads and installs the .txt
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements] # removes \n and spaces
        if '-e .' in requirements:
            requirements.remove('-e .')
        '''
        '-e' stands for editable mode: If you change your source code, you don’t need to reinstall the package — changes reflect immediately.
        '.' means current directory (your project folder where setup.py lives).
        So '-e .' tells pip:
        “Instead of just installing dependencies, also install this project itself (from the current directory) in editable mode using setup.py.”
        '''
    return requirements

setup(
    name='Pipeline',
    version='0.0.1',
    author='Yash',
    author_email='yashjain4284@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

