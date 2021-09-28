"""Write a Python program to print a dictionary line by line"""



students = {'Aex':{'class':'V',
                   'rolld_id':2},
            'Puja':{'class':'V',
                    'roll_id':3}}

for keys, values in students.items():
    print(keys)
    for keyz, valuez in values.items():
        print(keyz,":", valuez)

