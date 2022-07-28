peso = input("Peso en kg: ")
altura = input("Altura en m: ")
imc = round(float(peso) / float(altura) ** 2, 2)
print("Tu índice de masa corporal es " + str(imc) + ".")