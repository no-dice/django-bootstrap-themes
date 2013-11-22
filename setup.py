#!/usr/bin/env python

from setuptools import setup, find_packages

version = '3.0.5'

setup(
    name='django-bootstrap-themes',
    version=version,
    description="Bootstrap theme support for Django.",
    long_description=open("README.md", "r").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    keywords='django bootstrap themes',
    author='T. Scott Barnes',
    author_email='tsbarnes@tsbarnes.com',
    url='http://github.com/no-dice/django-bootstrap-themes',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'django>=1.4',
    ],
    include_package_data=True,
    zip_safe=False,
)
