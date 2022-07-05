c = float(input("Capital invertido: "))
i = float(input("Interes anual: "))
a = int(input("Años: "))
print("capital obtenido en la inversión: ", str(round(c *  (1+i/100)**a,2)))