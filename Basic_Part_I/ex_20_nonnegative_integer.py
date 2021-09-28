"""Write a Python program to get a string which is n (non-negative integer) copies of a given string."""

def nonnegative_int(liczba_str):
    return abs(int(liczba_str))


liczba_str = "-5"

print(nonnegative_int(liczba_str))


def nonnegative(text, n):
    result = ""
    for i in range(n):
        result = result + text
    return result


print(nonnegative("ciapong", 3))


def nonnegative_augmented(text, n):
    z = [""+text for i in range(n)]
    zz = "".join(z)
    return zz

print(nonnegative_augmented("ciapong", 5))
