"""Write a Python script to generate and print a dictionary that contains a number
 (between 1 and n) in the form (x, x*x)"""

dic = {}
n = int(input("Enter a number: "))

for x in range(1,n + 1):
        dic["{}".format(x)] = "{}".format(x*x)

for keys, values in dic.items():
    print(keys, values)
