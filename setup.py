try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='helloimports2',
    version='0.1.0',
    url='http://PROJECT URL',
    author='PROJECT AUTHOR',
    author_email='PROJECTAUTHOR@EXAMPLE.COM',
    description=('PROJECT DESCRIPTION GOES HERE'),
    license='PROJECT LICENSE GOES HERE, BSD, MIT, GPL, ETC.',
    packages=find_packages(), 
    install_requires=['nose'],
    # entry_points['console_scripts']  
    # is needed if you intend on having a cli executable(s)
    entry_points={ 
        'console_scripts': [
            'helloimports2=helloimports2:main',
        ],
    },
    # add classifiers below, see https://pypi.python.org/pypi/classifiers/
    # for classifier examples
    classifiers=[],
)
