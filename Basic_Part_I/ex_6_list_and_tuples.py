def tuples_and_lists(*args):
    lista = []
    for element in args:
        lista.append(element)
    return print("Tuple: ",args), print("List: ",lista)

args = 1,2,3,4

tuples_and_lists(*args)