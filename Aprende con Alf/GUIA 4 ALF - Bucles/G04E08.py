a = int(input("Escribe un nro entero positivo: "))
for i in range(1, a + 1, 2):
    for j in range(i, 0, -2):
        print(j, end = " ")
    print(" ")