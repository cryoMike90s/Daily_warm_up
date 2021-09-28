"""Write a Python program that will return true if the two given integer
 values are equal or their sum or difference is 5"""

def true_or_nothing(a,b):
    if (a == b) or ((a + b) == 5) or (abs(a - b) == 5):
        return True
    else:
        pass

print(true_or_nothing(3,2))