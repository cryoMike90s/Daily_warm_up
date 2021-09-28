"""Write a Python program to input a number, if it is not a number generates an error message."""

def give_me_number(number:int):
    if type(number) == int:
        return print(number)
    else:
        raise TypeError("This is not a number")

# give_me_number("xdd")


def give_me_number_2():
    while True:
        try:
            a = int(input("Please give a number: "))
            print(a)
            break
        except ValueError:
            print("This is not a number")

give_me_number_2()