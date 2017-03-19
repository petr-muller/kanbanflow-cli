# pylint: disable=missing-docstring,import-error,no-name-in-module

from distutils.core import setup

setup(name='kbfcli',
      version='0.1',
      py_modules=['kbfcli'],
      scripts=['bin/kbf.py'],
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5'
          ])
