#!/usr/bin/env python
try:
    from setuptools import setup
    args = {}
except ImportError:
    from distutils.core import setup
    print("""\
    *** WARNING: setuptools is not found.  Using distutils...
    """)

from setuptools import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

from os import path
setup(name='gblearn',
    version='0.1.0',
    description='Scientific code to represent a collection of atomic environments',
    #long_description= "" if not path.isfile("README.md") else read_md('README.md'),
    author='Jay Spendlove',
    author_email='jayclark24@gmail.com',
    url='https://github.com/msg-byu/gblearn',
    license='Academic Public License',
    setup_requires=['pytest-runner',],
    tests_require=['pytest', 'python-coveralls'],
    install_requires=[
        "numpy",
        "tqdm",
        "ase",
        "pycsoap",
        "annoy"
    ],
    packages=['gblearn'],
    scripts=[],
    package_data = {'gblearn': []},
    include_package_data=False,
    classifiers=[
        'Development Status :: 1 - planning',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: POSIX::Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    )
