"""Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
 and the values are square of keys."""

dictionary = {}

for x in range(1,16):
    dictionary["{}".format(x)] = "{}".format(x*x)

for keys, values in dictionary.items():
    print(keys, values)
    