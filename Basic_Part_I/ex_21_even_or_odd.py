"""Write a Python program to find whether a given number (accept from the user) is even or odd,
 print out an appropriate message to the user."""

def even_or_odd(number):
    if (number % 2 == 0) and (number > 0):
        print("The number is even")
    elif number == 0:
        print("This is zero")
    else:
        print("The number is odd")

number = 5

even_or_odd(number)