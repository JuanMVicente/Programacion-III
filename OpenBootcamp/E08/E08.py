numInicial = 2
numFinal = 8
lista = []

for num in range(numInicial,numFinal+1,1):
    if num % 2 == 1:
        lista.append(num)

print(lista)

