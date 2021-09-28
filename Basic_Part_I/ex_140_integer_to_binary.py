"""Write a Python program to convert an integer to binary keep leading zeros."""

def leading_zeros(number:int):
    a = format(number, '08b') #W sumie to to '08b' to jest ten *kwargs czyli styl więc się zgada
    if a[0] == '0':
        print(a)
    else:
        print("invalid")

numer = 12
leading_zeros(numer)

print("{} --- {}".format(format(numer, '08b'), bin(numer)))