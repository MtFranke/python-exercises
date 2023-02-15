"""
Write a Python program to locate Python site packages.
"""
from distutils.sysconfig import get_python_lib

print(get_python_lib())