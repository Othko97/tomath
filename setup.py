from setuptools import setup, find_packages

setup(name='ToMath',
      description='A python package for mathematics',
      packages=find_packages(exclude='tests')
#          tests_require=['pep8',
#                         'pytest-pep8',
#                         ]
)

