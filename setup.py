from distutils.core import setup

setup(
    name='SignedEmailMessage',
    version='0.1.0',
    author='Jakub Wasielak',
    author_email='kuba.wasielak@gmail.com',
    packages=['django-sem'],
    scripts=[],
    url='http://pypi.python.org/pypi/SignedEmailMessage/',
    license='LICENSE.txt',
    description='Useful tool for sending signed emails.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.1.1",
        "M2Crypto>=0.21.1",
    ],
)