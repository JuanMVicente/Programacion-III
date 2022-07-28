'''Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la 
función dada a cada uno de los elementos de la lista.'''

def funcionLista(Funcion,Lista):
    l = []
    for i in lista:
        l.append(Funcion(i))
    return l

def cuadrado(x):
    return x*x

lista=[2,5,7,9]

print(funcionLista(cuadrado,lista))