"""Write a Python program to test whether a passed letter is a vowel or not."""

def is_it_vowel(letter):
    vowels = ("A", "E", "I", "O", "U", "Y")
    letter = letter.upper()
    if letter in vowels:
        print("Entered letter is vowel")
    else:
        print("Is not a vowel")

is_it_vowel("B")
