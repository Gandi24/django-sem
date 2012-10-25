from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-sem',
    version='0.2.1',
    author='Jakub Wasielak',
    author_email='kuba.wasielak@gmail.com',
    packages=find_packages(),
    scripts=[],
    url='http://pypi.python.org/pypi/SignedEmailMessage/',
    license='LICENSE.txt',
    description='Useful tool for sending signed emails.',
    long_description=open('README.txt').read(),
    include_package_data=True,
    install_requires=[
        "Django >= 1.1.1",
        "M2Crypto>=0.21.1",
    ],
)