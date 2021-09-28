"""Write a Python program to retrieve file properties."""

import os

print(os.path.getsize(__file__))
print(os.path.getmtime(__file__))
print(os.path.getctime(__file__))
print()
print(os.stat(__file__))
