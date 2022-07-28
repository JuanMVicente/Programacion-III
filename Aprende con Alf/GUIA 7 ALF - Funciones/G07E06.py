def prom(lista):
    # l = lista.split(",")
    # suma = 0
    # for i in range(len(l)):
    #     suma += l[i]
    return sum(lista)/len(lista)

# a = input("Escribe una lista: ")
print(prom([12, 34, 16]))
print(prom([1, 2, 3, 4, 5]))
print(prom([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))