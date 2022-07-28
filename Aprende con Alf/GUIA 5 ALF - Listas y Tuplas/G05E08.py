a = input("Escriba una palabra: ")
b = a
a = list(a)
b = list(b)
b.reverse()
if a == b:
    print("Es palíndromo.")
else:
    print("No es palíndromo.")