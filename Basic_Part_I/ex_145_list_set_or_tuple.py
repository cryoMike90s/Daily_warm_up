"""Write a Python program to test if a variable is a list or tuple or a set."""

obj = (0,)

if isinstance(obj, list):
    print("List")
elif isinstance(obj, tuple):
    print("Tuple")
elif isinstance(obj, dict):
    print("Dict")
else:
    print("Something went wrong")