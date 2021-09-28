"""Write a Python program to replace dictionary values with their average."""

student_details= [
    {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
    {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
    {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]

def average_me(number_1: float, number_2: float):
    number_3 = (number_2 + number_1)/2
    return number_3



for i in student_details:
    i['average'] = average_me(i['V'], i['VI'])
    i.pop('V')
    i.pop('VI')


print(student_details)
