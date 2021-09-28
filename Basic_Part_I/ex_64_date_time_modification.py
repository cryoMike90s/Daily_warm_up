"""Write a Python program to get file creation and modification date/times."""

import os.path
import time

def give_me_that_date():
    return print("The file {} was created on {} and modified lat time at {}".format(
        os.path.relpath("Basic_Part_I/ex_63_absolute_path.py"),
        time.ctime(os.path.getctime("Basic_Part_I/ex_63_absolute_path.py")),
        time.ctime(os.path.getmtime("Basic_Part_I/ex_63_absolute_path.py"))
    ))

give_me_that_date()