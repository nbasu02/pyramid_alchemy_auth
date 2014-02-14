from setuptools import setup, find_packages
import os
from distutils.util import convert_path

import pyramid_alchemy_auth

def find_packages(where='.', exclude=()):
    """Return a list all Python packages found within directory 'where'

    'where' should be supplied as a "cross-platform" (i.e. URL-style) path; it
    will be converted to the appropriate local path syntax.  'exclude' is a
    sequence of package names to exclude; '*' can be used as a wildcard in the
    names, such that 'foo.*' will exclude all subpackages of 'foo' (but not
    'foo' itself).
    """
    out = []
    stack=[(convert_path(where), '')]
    while stack:
        where,prefix = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where,name)
            looks_like_package = (
                '.' not in name
                and os.path.isdir(fn)
            )
            if looks_like_package:
                out.append(prefix+name)
                stack.append((fn, prefix+name+'.'))
    for pat in list(exclude)+['ez_setup']:
        from fnmatch import fnmatchcase
        out = [item for item in out if not fnmatchcase(item,pat)]
    return out

here = os.path.dirname(os.path.realpath(__file__))
readme = os.path.join(here, 'README.txt')

setup(
    name='pyramid_alchemy_auth',
    version='0.1.0',
    author='Neil Basu',
    author_email='nbasu02@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*_tmpl']},
    zip_safe=False,
    scripts=[],
    url='',
    license='LICENSE.txt',
    description='Pyraid app with Beaker pre-configured.',
    long_description=open(readme).read(),
    install_requires=[],
    entry_points='''
    [pyramid.scaffold]
    alchemy_auth=pyramid_alchemy_auth.scaffolds:AlchemyAuthTemplate
    '''
)