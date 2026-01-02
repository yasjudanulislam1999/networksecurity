from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of requirements
    """
    requirement_lst:List[str]=[]

    try:
        with open('requirements.txt') as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()
                
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requrements.txt does not exist')

    return requirement_lst

print(get_requirements())


setup(
    name = 'Network Security',
    version = '0.0.1',
    author = 'Yasjudan Ul Islam',
    author_email='yasjudanulislam1999@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements()
)

