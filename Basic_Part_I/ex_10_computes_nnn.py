def compute_me(n):
    z = n + eval("{0}{0}".format(n)) + eval("{0}{0}{0}".format(n))
    return z

print(compute_me(5))

