d = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
suma = 0
for a, b in d.items():
    print(a, " tiene ", b, "creditos.")
    suma += b
print(suma, " es el total de créditos.")