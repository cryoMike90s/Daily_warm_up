"""Write a Python program to sum all the items in a dictionary."""

dic1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

a = sum(dic1.keys())
b = sum(dic1.values())

c = a + b
print(c)


