"""Write a Python program to sort three integers without using conditional statements and loops."""

def sort_me(number_1, number_2, number_3):
    a3 = max(number_1, number_2, number_3)
    a1 = min(number_1, number_2, number_3)
    a2 = (number_1 + number_2 + number_3) - a1 - a3
    return print(a1, a2, a3)


number_1 = int(input("Number 1: "))
number_2 = int(input("Number 2: "))
number_3 = int(input("Number 3: "))

sort_me(number_1, number_2, number_3)