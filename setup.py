#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for remove-emoji CLI tool
"""

from setuptools import setup

setup(
    name='remove-emoji',
    version='1.0.0',
    description='移除文件中的 emoji 字符的命令行工具',
    author='Your Name',
    py_modules=['remove_emoji'],
    entry_points={
        'console_scripts': [
            'remove-emoji=remove_emoji:main',
        ],
    },
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)

