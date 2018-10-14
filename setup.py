# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 12:09:04 2018

@author: David
"""

from setuptools import setup

setup(
      name=     'template_python_projects',
      version=  '1.1',
      
      # find_packages() can be imported and used here
      packages= ['sound', 'sound.effects', 'sound.formats', 'sound.filters'],
      
      scripts= ['bin/testing_sound.py'],
      
      author= 'djclavero',
      author_email= 'djclavero@yahoo.com',
      
      license= 'MIT',
      long_description= open('README.txt').read(),
      
      keywords = ['projects', 'test'],
      
      url= 'https://pypi.org/project/template_python_projects',
      
      description= 'Template project in python',
      
      # Dependences
      install_requires= ['', ''],
      
)

