"""Write a Python program to print all unique values in a dictionary."""

original_list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

unique = set(val for dic in original_list for val in dic.values())
print(unique)