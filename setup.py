#!/usr/bin/env python

from distutils.core import setup

setup(name='Github-review',
      version='1.0',
      description='Scripts to ease review process',
      requires= ['sh', 'GitPython', 'PyGithub'],
      scripts = ['github-review']
     )
