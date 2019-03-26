# -*- coding: utf-8 -*-
# Copyright (c) Sebastian Klaassen. All Rights Reserved.
# Distributed under the MIT License. See LICENSE file for more info.

import os.path
import setuptools
import qt5frames

def read(filename, begin_after=None):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        content = file.read()

    if begin_after and begin_after in content:
        content = content[content.find(begin_after) + len(begin_after):]

    return content

setuptools.setup(
    name='qt5frames',
    packages=['qt5frames'],
    version=qt5frames.__version__,  
    description='Frame classes for Qt5',
    long_description=read('README.md'),
    author='Sebastian Klaassen',
    author_email='rcsepp@hotmail.com',
    license='MIT',
    url='https://github.com/RcSepp/asyncframeworks/official/qt5frames',
    classifiers=[
        #'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ],
    python_requires='>=3.5',
    install_requires=['asyncframes', 'PyQt5', 'multipledispatch', 'numpy', 'numpy-quaternion'],
)
