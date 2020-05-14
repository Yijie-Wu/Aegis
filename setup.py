# -*- encoding:utf-8 -*-
"""
Author: Yijie.Wu
Email: 1694517106@qq.com
Date: 2020/5/14 14:08
"""

from setuptools import find_packages
from setuptools import setup

setup(
    name="aegis",
    version=0.1,
    description="一个微型测试框架",
    long_description=open("README.md", 'r').read(),
    long_description_content_type="text/markdown",
    author='Yijie.Wu',
    author_email="1694517106@qq.com",
    url="https://github.com/Yijie-Wu/",
    project_urls={
        "Github": "https://github.com/Yijie-Wu/Aegis",
    },
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={"Aegis": "Aegis"},
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords="Micro Test Framework",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Testing :: Unit",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "License :: OSI Approved :: MIT",
        "Natural Language :: Chinese (Simplified)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ]
)
