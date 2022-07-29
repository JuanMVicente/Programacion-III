'''Escribir un programa que almacene las matrices en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.'''


def multiplica_matriz(a,b):
    resultado =[]
    if a[0].__len__() == b.__len__():
        for i in range(0,a.__len__()):
            c = []
            for j in range(0,b[0].__len__()):
                c.append(0)
            resultado.append(c)
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    resultado[i][j] += a[i][k] * b[k][j]
        for i in range(len(c)):
            resultado[i] = tuple(resultado[i])
        resultado = tuple(resultado)
        return resultado
            


a = ((1, 2, 3), (4, 5, 6))
b = ((-1, 0), (0, 1), (1, 1))
print(multiplica_matriz(a,b))