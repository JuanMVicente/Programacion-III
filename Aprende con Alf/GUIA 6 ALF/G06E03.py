p = {"Plátano": "1.35", "Manzana": "0.80", "Pera": "0.85", "Naranja": "0.70"}
f = input("Fruta: ")
k = float(input("Peso (kg): "))
if f in p:
    print(str(k) + " kilos de " + str(f) + " valen " + str(float(p[f])*k) + ".")
else:
    print("La fruta no esta disponible.")