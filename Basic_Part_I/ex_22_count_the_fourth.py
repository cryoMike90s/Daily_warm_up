"""Write a Python program to count the number 4 in a given list. """

def count_four(list):
    # occurances = list.count("4")
    return "There are {} numbers '4' in a list".format(list.count("4"))

list = ["12","11","10","4","111","2222", "4"]

print(count_four(list))


def count_foour_for_numbers(list):
    count = 0
    for i in list:
        if i == 4:
            count += 1
    return count


list2 = [12,122,4,5,4]

print(count_foour_for_numbers(list2))