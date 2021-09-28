"""Write a Python program to find out the number of CPUs using."""

import multiprocessing

def CPU_number():
    return multiprocessing.cpu_count()

print(CPU_number())