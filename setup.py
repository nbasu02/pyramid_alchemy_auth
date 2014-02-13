from setuptools import setup, find_packages

setup(
    name='pyramid_alchemy_auth',
    version='0.1.0',
    author='Neil Basu',
    author_email='nbasu02@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=[],
    url='',
    license='LICENSE.txt',
    description='Pyraid app with Beaker pre-configured.',
    long_description=open('README.txt').read(),
    install_requires=[],
    entry_points='''
    [pyramid.scaffold]
    alchemy_auth=pyramid_alchemy_auth.scaffolds:AlchemyAuthTemplate
    '''
)