import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='meshcut',
    version='0.1',
    description='Utilities to slice 3D triangular meshes.',
    long_description=read('README.rst'),
    author='Julien Rebetez',
    author_email='julien@fhtagn.net',
    url='https://github.com/julienr/meshcut',
    keywords = ['mesh', 'slice', 'cross-section', '3D', 'triangular'],
    py_modules=['meshcut'],
)
