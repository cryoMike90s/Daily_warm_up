"""Write a Python program to check whether a file path is a file or a directory."""

import os
import glob

def file_or_directory(path_v:str):
    if os.path.isdir(path_v):
        print('The file is directory')
    else:
        print("File is not directory")


file_or_directory('Basic_Part_I/ex_2_python_version.py')