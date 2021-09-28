"""Write a Python program to get an absolute file path"""

import os

abs_path = os.path.abspath(os.path.relpath(__file__))
print(abs_path)