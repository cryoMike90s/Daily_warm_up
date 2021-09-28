"""Write a Python program to test whether all numbers of a list is greater than a certain number. """

def greater_than(lista:list, number:int):
    for x in lista:
        if number > x:
            yield print("Yes".format(x))
            break
        print("No")
        break


przyklad = greater_than([6,7,6,6], 5)

for z in przyklad:
    z