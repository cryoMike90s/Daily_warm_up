"""Write a Python program to find path refers to a file or directory when you encounter a path name."""

import os

def find_path(name):
    return print(os.path.abspath(name))

name = "ex_107_file_properties.py"
find_path(name)