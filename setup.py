from setuptools import setup, find_packages

def get_requirements(file_path):
    requirements= []
    
    with open(file_path) as f:
        requirements= f.readlines()
        requirements= [r.replace("\n","")for r in requirements]
    return requirements


setup(
    name='New_Project',
    version='0.0.1',
    description='Machine Learning Model deployment Pipeline learning',
    author='Hafsa Nizami',
    author_email='hafsanizami24@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)