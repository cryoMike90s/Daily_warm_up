"""Write a Python program to list home directory without absolute path"""

import os

x = os.listdir('..')
print(x)