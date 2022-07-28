c = float(input("Capital invertido: "))
t = float(input("Tasa (%): "))
a = int(input("Años: "))
for i in range(a):
    print("Al año " + str(i+1) + " obtiene un capital de " + str(round(c*(1+t/100)**(i+1), 2)) + " $.")