"""Write a Python function to check whether a number is divisible by another number.
 Accept two integers values form the user."""

def is_divisible(a, b):
    if a % b == 0 or b % a == 0:
        return print("Is divisible")
    else:
        return print("Not divisible")

is_divisible(int(input("Enter first number: ")),int(input("Enter second number: ")))