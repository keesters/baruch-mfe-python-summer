from setuptools import setup, find_packages

setup(
    name='cbapi',
    packages=['cbapi'],
    url='https://github.abc.com/abc/myabc',
    description=CrunchBase API for pulling people and organization data',
    long_description=open('README.md').read(),
    install_requires=[
        "requests==2.7.0",
        "SomePrivateLib>=0.1.0",
        ],
    dependency_links = [
     "git+git://github.abc.com/abc/SomePrivateLib.git#egg=SomePrivateLib",
    ],
    include_package_data=True,
)
