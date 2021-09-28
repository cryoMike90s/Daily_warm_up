"""Write a Python program to print out a set containing all the colors from color_list_1 which
are not present in color_list_2"""

def not_present_in_second_set(set_1, set_2):
    return set_1.difference(set_2)


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(not_present_in_second_set(color_list_1, color_list_2))

