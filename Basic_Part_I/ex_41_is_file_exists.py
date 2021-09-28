"""Write a Python program to check whether a file exists."""

import glob
import os.path

def chec_if_exists(path):
    if path in glob.glob("Basic_Part_I/*.py"):
        return True
    return "File doesn't exists"

def check_if_exists_2(path):
    if os.path.isfile(path):
        return True
    return "File doesn't exists"

print(chec_if_exists("Basic_Part_I\\ex_38_solve_equation.py"))
print(check_if_exists_2('Basic_Part_I/ex_38_solve_equation.py'))

