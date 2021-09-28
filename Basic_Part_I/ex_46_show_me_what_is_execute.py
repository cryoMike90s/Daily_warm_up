"""Write a python program to get the path and name of the file that is currently executing."""

import os

def get_my_path():
    return os.path.abspath(__file__)


print(get_my_path())

