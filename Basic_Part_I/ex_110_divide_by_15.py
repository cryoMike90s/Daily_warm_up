"""Write a Python program to get numbers divisible by fifteen from a list using an anonymous function."""

new_list = list(filter(lambda x: (x % 15 == 0) and (x != 0) , range(150)))
print(new_list)


