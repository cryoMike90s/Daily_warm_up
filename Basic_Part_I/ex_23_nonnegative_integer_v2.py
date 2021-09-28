"""Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
Return the n copies of the whole string if the length is less than 2."""

def nonnegative(text, n):
    if len(text) < 2:
        z = ["" + text for i in range(n)]
        zz = "".join(z)
    else:
        z = ["" + text[0:2] for i in range(n)]
        zz = "".join(z)
    return zz


text = "z"

print(nonnegative(text, 3))