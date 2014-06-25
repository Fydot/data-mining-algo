#!/usr/bin/python
# coding: utf-8
from setuptools import setup, find_packages


setup(name='mining',
      version='0.0.1',
      author='huangdiandian',
      author_email='hdd@zhihu.com',
      description='mining',
      license='PRIVATE',
      packages=find_packages('mining'),
      package_dir={'': 'mining'},
      install_requires=[
              'redis',
      ],
      entry_points={
          'console_scripts': [
          ],
      },)
