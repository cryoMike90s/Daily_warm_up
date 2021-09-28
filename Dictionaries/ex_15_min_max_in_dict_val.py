"""Write a Python program to get the maximum and minimum value in a dictionary."""

dic1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

a = max(dic1.items(), key=lambda x:x[0])
print(a)

b = min(dic1.items(), key=lambda x:x[0])
print(b)