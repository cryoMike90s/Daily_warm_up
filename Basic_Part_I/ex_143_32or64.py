""" Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system."""

import platform

print(platform.architecture()[0])