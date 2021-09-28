"""Write a Python program to extract the filename from a given path."""

import os

def give_me_file_name(path):
    return print(os.path.split(os.path.relpath(path))[1])

path = "Basic_Part_I/ex_81_concat_N_strings.py"

give_me_file_name(path)


def give_me_file_name_2(path):
    return print(os.path.basename(path))

give_me_file_name_2(path)