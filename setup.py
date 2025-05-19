from setuptools import setup, find_packages

with open("requirement.txt", "r") as _f:
    requirement=[line for line in _f.read().split('\n')]

setup(
    name='summarization',
    description='python CLI tools for summarization using hugging face',
    version='0.1.0',
    packages=find_packages(),
    author='Alish-Giri',
    author_email='alishgiri29@gmail.com',
    url='https://github.com/alishgiri369/Text-Summarization-with-CLI_Tools',
    install_requires=requirement,
    entry_points='''
    [console_scripts]
    summarize=summarize.main:main
    '''


)
