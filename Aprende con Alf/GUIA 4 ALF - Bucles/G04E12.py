f = input("Escriba una frase: ")
l = input("Elija una letra: ")
contador = 0
for i in f:
    if i == l:
        contador += 1
print("La letra " + l + " se encuentra " + str(contador) + "  veces en la frase: " + f + ".")