from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT ='-e .' #'-e .' if we have this in the requirements.txt then it will automatically call the setup.py
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        #requirements = [req.strip() for req in file_obj.readlines()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name='StudentPerformancePrediction',
    version='0.0.1',
    author='ChenchaiahMekalathuru',
    author_email='mekalathuru.chenchaiah@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')    #intead of this install_requires=['pandas', 'numpy', 'seaborn']
)
