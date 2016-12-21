from setuptools import setup, find_packages

import config_manager


def readme():
    with open("README.md") as f:
        return f.read()


setup(name='config-manager',
      version=config_manager.__version__,
      description='A basic config manager',
      long_description=readme(),
      url='https://github.com/afxentios/basic-config_manager',
      author=config_manager.__author__,
      author_email='afxentios.hadjiminas@gmail.com',
      packages=find_packages(),
      install_requires=['PyYAML', 'simplejson', 'mock'])
