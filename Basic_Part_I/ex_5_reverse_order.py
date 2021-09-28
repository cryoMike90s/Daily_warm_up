def reverse_order_function(name, surname):
    reverse = "{} {}".format(surname, name)
    return print(reverse)

name = input("Give name:" )
surname = input("Give surname: ")

reverse_order_function(name, surname)
