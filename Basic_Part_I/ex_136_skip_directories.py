"""Write a Python program to find files and skip directories of a given directory."""

import fnmatch
import os
import glob

pattern = "*file*"

for x in glob.glob('Basic_Part_I/*'):
    if not fnmatch.fnmatch(x, pattern):
        print(os.path.basename(x))
