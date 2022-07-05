def cuadrado(*lista):
    list = []
    for i in lista:
        list.append(i**2)
    return list

def estadisticos(*lista):
    est = {}
    est["media"] = sum(lista)/len(lista)
    est["varianza"] = sum(cuadrado(*lista))/len(lista) - est["media"]**2
    est["desviacion"] = est["varianza"]**0.5
    return est

# a = input("Escribe una lista: ")
print(estadisticos(12, 34, 16))
print(estadisticos(11, 12, 15, 14))