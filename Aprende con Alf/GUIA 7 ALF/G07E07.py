def cuadrados(lista):
    list = []
    for i in lista:
        list.append(i**2)
    return list

# a = input("Escribe una lista: ")
print(cuadrados([12, 34, 16]))