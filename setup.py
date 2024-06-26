from setuptools import find_packages, setup
from typing import List


Hyphen = '-e .'
def get_requirements(file_path:str) ->List[str]:
    """this function returns the list of requirements
    """
    requirements= []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements = [req.replace('/n','') for req in requirements]
        if Hyphen in requirements:
            requirements.remove(Hyphen)
    return requirements


setup(name='ML Project',
      version='0.0.1',
      author='Rahul Manocha',
    author_email='rahul.rmanocha@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
    )



    
    