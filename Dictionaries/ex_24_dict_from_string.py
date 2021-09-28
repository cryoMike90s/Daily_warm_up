"""Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string."""

string = "W3resource"
dict_from_string = {}

for y in string:
    z = string.count(y)
    dict_from_string[y] = z


print(dict_from_string)



