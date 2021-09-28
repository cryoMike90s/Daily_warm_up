""" Write a Python program to sort files by date"""

import os
import time
from datetime import datetime
import glob

######DRAFT########

# x = time.ctime(os.path.getctime("Basic_Part_I/for_ex_70/first_file.py"))
# print(x)
# y = time.ctime(os.path.getctime("Basic_Part_I/for_ex_70/third_file.py"))
# y1 = datetime.strptime(y, "%a %b %d %H:%M:%S %Y")

# lista = []
# lista_name = []
#
# for z in glob.glob("Basic_Part_I/for_ex_70/*"):
#     z2 = datetime.strptime(time.ctime(os.path.getctime(z)), "%a %b %d %H:%M:%S %Y")
#     # z3 = z2, z
#     lista.append((z2, z))
#
# print(lista)
# z = sorted(lista)
# print(z)

#################

####SOLUTION_1######
def sort_my_files():
    return sorted([(datetime.strptime(time.ctime(os.path.getctime(z)), "%a %b %d %H:%M:%S %Y"), z) for z in
                   glob.glob("Basic_Part_I/for_ex_70/*")])

print(sort_my_files())


####SOLUTION_2######
def sort_my_files_xd():
    files = glob.glob("Basic_Part_I/for_ex_70/*")
    files.sort(key=os.path.getctime)
    return print("\n".join(files))

sort_my_files_xd()