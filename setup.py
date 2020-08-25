from __future__ import print_function
from setuptools import setup
from teslaapi import __version__, __author__
setup(
    name="tesla-api-py",
    version=__version__,
    author=__author__,
    author_email="zcq100@gmail.com",
    description="Tesla api ",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="Apache License",
    url="https://github.com/zcq100/teslaapi",
    packages=['teslaapi'],


    classifiers=[
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.6',
    ],
)
