'''Escribir una función que calcule el módulo de un vector.'''

def modulo(vector):
    suma = 0
    for i in vector:
        suma = suma + i**2
    return suma ** 0.5

print(modulo((3, 4)))
print(modulo((1, 2, 3)))