import os
import sys
from setuptools import setup

README = open('README').read()


def get_version():
    """ Copied from @nvie:

    https://github.com/nvie/rq/blob/master/setup.py
    I'm toooooo lazy ...
    """
    basedir = os.path.dirname(__file__)
    try:
        with open(os.path.join(basedir, 'gists/version.py')) as f:
            version = None
            exec(f.read())
            return version
    except Exception:
        raise RuntimeError('No version info found.')


requirements = ['requests == 2.19.1', 'clint == 0.3.1', 'urllib3']
if sys.version_info < (2, 7):
    requirements.append('argparse')
elif sys.version_info < (2, 6):
    raise Exception('Must use python 3.6 or greater')

setup(name='gists',
      packages=['gists'],
      version=get_version(),
      author='Jaume Devesa',
      author_email='jaumedevesa@gmail.com',
      url='http://jdevesa.github.com/gists',
      description='CLI interface to manage Github gists',
      install_requires=requirements,
      scripts=['gists/gists'],
      include_package_data=True,
      long_description=README,
      license='MIT',
      test_suite='tests',
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.6",
          "Development Status :: 5 - Production/Stable ",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Operating System :: POSIX :: Linux"
      ])
