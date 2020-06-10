from distutils.core import setup

setup(
    name='CogUtils',
    version='0.1dev',
    author='David Kincaid',
    author_email='dlkincaid0@gmail.com',
    packages=['cogutils',],
    install_requires=['dotmap',],
    license='MIT',
    long_description=open('README.md').read(),
)