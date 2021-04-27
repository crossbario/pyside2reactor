#!/usr/bin/env python

# When pip installs anything from packages, py_modules, or ext_modules that
# includes a twistd plugin (which are installed to twisted/plugins/),
# setuptools/distribute writes a Package.egg-info/top_level.txt that includes
# "twisted".  If you later uninstall Package with `pip uninstall Package`,
# pip <1.2 removes all of twisted/ instead of just Package's twistd plugins.
# See https://github.com/pypa/pip/issues/355 (now fixed)
#
# To work around this problem, we monkeypatch
# setuptools.command.egg_info.write_toplevel_names to not write the line
# "twisted".  This fixes the behavior of `pip uninstall Package`.  Note that
# even with this workaround, `pip uninstall Package` still correctly uninstalls
# Package's twistd plugins from twisted/plugins/, since pip also uses
# Package.egg-info/installed-files.txt to determine what to uninstall,
# and the paths to the plugin files are indeed listed in installed-files.txt.

import os
from distutils import log
from setuptools import setup
from glob import glob


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: X11 Applications :: Qt',
    'Framework :: Twisted',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Natural Language :: English',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

setup(
    name='pyside2reactor',
    version='21.4.1',
    license='MIT',
    classifiers=classifiers,
    author='Crossbar',
    description='Twisted integration with PySide6 (Qt6) and PySide2 (Qt5)',
    long_description=read('README.rst'),
    url='https://github.com/crossbario/pyside2reactor',
    download_url='https://github.com/crossbario/pyside2reactor/tarball/master/',
    packages=[
        'pyside2reactor',
        'twisted.plugins',
    ],
    py_modules=['pyside2reactor'],
    keywords=['Qt', 'twisted', 'pyside'],
    install_requires=['twisted']
)
