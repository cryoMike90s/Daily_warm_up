"""Write a Python program to convert height (in feet and inches) to centimeters"""

def convert_me(h):
    if not "," in h:
        inches = float(h) * 12
        cm = inches * 2.54
        return print(cm)
    return print("Use poin instead of comma ")

convert_me(input("Plese enter a height in foots: "))



