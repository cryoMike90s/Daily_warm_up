"""Write a Python program to round a floating-point number to specified number decimal places."""

def round_me_please(float_number:float):
    return round(float_number, 3)

print(round_me_please(3.111112212))