def area_circulo(radio):
    pi = 3.1416
    return pi* radio**2

def vol_cilindro(radio, altura):
    return area_circulo(radio) * altura

r = input("Radio: ")
h = input("Altura: ")
print(round(area_circulo(float(r)), 2))
print(round(vol_cilindro(float(r), float(h)), 2))