"""Write a Python program to make file lists from current directory using a wildcard."""

import os
import glob
import fnmatch

pattern = "*file*"

for x in glob.glob("Basic_Part_I/*"):
    if fnmatch.fnmatch(x,pattern):
        print(os.path.basename(x))

print(40*"*")

ina = [print(os.path.basename(x)) for x in glob.glob("Basic_Part_I/*") if fnmatch.fnmatch(x, pattern)]

for z in ina:
    z