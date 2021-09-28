"""Write a Python program to divide a path on the extension separator."""

import os

def divide_from_extension(path):
    basename = os.path.basename(path)
    only_name = basename.split(".")
    return print(only_name[0])


path = 'Basic_Part_I/ex_92_special_character.py'
divide_from_extension(path)