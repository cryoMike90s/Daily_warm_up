"""Write a Python program to check a dictionary is empty or not."""

vehicles = {}

if all(vehicles) and bool(vehicles):
    print("Not empty")
else:
    print("Empty")