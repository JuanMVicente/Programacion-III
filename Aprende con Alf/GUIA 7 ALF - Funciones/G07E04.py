def iva(costo, porcentaje=21):
    print(round(costo * (1 + porcentaje/100), 2))
    return

c = input("Costo: ")
p = input("Porcentaje: ")
if p != "":
    iva(float(c), float(p))
else:
    iva(float(c),)