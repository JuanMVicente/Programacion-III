'''Escribir una función que reciba otra función booleana y una lista, 
y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.'''

from re import L


def funcionBooleanaLista(funcion,lista):
    l=[]
    for i in lista:
        if funcion(i):
            l.append(i)
    return l

def pares(x):
    return x%2==0

l2=[1, 2, 3, 4, 56 ,7 ,8 , 54, 9]

print(funcionBooleanaLista(pares,l2))