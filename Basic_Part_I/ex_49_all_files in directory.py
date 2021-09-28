"""Write a Python program to list all files in a directory in Python."""

import glob

def list_all_files(path):
    return glob.glob(path)

print(list_all_files("Basic_Part_I/*"))