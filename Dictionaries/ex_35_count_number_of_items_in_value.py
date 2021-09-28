""" Write a Python program to count number of items in a dictionary value that is a list."""

dict_1 = {'n1': [2, 3, 1], 'n2': [2, 3, 1, 0] }

tick_toe=0
for i,j in dict_1.items():
    numbero = len(j)
    tick_toe += numbero
    print("Number of items in {} is".format(i), numbero)


print("Finally there are {} objects".format(tick_toe))

#Inaczej

ctr = sum(map(len, dict_1.values()))
print(ctr)