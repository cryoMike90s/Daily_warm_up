"""Write a Python program to count the values associated with key in a dictionary. """

d1 = {'a': 600, 'b': 200, 'c':100, 'd':400, 'e':500}


a = str(input("Please choose a keys from dictionary to sum: "))
b = str(input("Please choose a keys from dictionary to sum: "))

sum = d1.get(a) + d1.get(b)
print(sum)

# print(d1.get('a'))