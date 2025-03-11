# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright © Griffin Project Contributors
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Setup script for pyls_griffin."""

# Standard library imports
import ast
import os
import os.path as osp

# Third party imports
from setuptools import find_packages, setup

HERE = osp.dirname(osp.abspath(__file__))


def get_version(module='pyls_griffin'):
    """Get version."""
    with open(os.path.join(HERE, module, '__init__.py'), 'r') as f:
        data = f.read()
    lines = data.split('\n')
    for line in lines:
        if line.startswith('VERSION_INFO'):
            version_tuple = ast.literal_eval(line.split('=')[-1].strip())
            version = '.'.join(map(str, version_tuple))
            break
    return version


def get_description():
    """Get long description."""
    with open(os.path.join(HERE, 'README.md'), 'r') as f:
        data = f.read()
    return data


REQUIREMENTS = ['python-lsp-server >= 1.0.1']

setup(
    name='pyls-griffin',
    version=get_version(),
    keywords=['PyLSP', 'Plugin'],
    url='https://github.com/griffin-ide/pyls-griffin',
    license='MIT',
    author='Griffin Project Contributors',
    author_email='griffin.python@gmail.com',
    description='Griffin extensions for the python-lsp-server',
    long_description=get_description(),
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    python_requires='>= 3.6',
    install_requires=REQUIREMENTS,
    include_package_data=True,
    entry_points={"pylsp": ["pyls_griffin = pyls_griffin.plugin"]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ])
