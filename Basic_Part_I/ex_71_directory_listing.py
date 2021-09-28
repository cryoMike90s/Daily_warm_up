"""Write a Python program to get a directory listing, sorted by creation date."""

import os
import glob


def list_by_date():
    directories = glob.glob(r"C:\Users\Dell\Desktop\Pytong\W3_school\*")
    directories.sort(key=os.path.getctime)
    final_directories = []
    for x in directories:
        if os.path.isdir(x):
            final_directories.append(x)

    return print("\n".join(final_directories))


list_by_date()

print(40*"*")

def list_by_date2():
    directories = glob.glob(r"C:\Users\Dell\Desktop\Pytong\W3_school\*")
    directories.sort(key=os.path.getctime)
    return print("\n".join([x for x in directories if os.path.isdir(x)]))

list_by_date2()